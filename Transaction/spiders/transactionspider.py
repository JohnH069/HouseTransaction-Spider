import scrapy
import requests
import lxml.html
import re
import json
import datetime
from Transaction.items import TransactionItem

  
class TransactionspiderSpider(scrapy.Spider):
    name = 'transactionspider'
    allowed_domains = ['sh.lianjia.com/chengjiao/']
    #start_urls = ['https://sh.lianjia.com/chengjiao/pudong']
    
    
    
    def start_requests(self):                               # 构建Start_Request
        ini_url = 'https://sh.lianjia.com/chengjiao/'
        content = requests.get(ini_url).content.decode()
        selector = lxml.html.fromstring(content)
   
        part_urls = selector.xpath('//div[@data-role="ershoufang"]/div/a/@href')
        start_urls = ['https://sh.lianjia.com/chengjiao'+part_url for part_url in part_urls]
        for start_url in start_urls:
            yield scrapy.Request(start_url, callback=self.parse) 
    
    
    
    def parse(self, response):
        item = TransactionItem()
        district = response.xpath('//div[@class="total fl"]/text()').extract()[1][1:3]
        transactions = response.xpath('//li/div[@class="info"]')  
        for transaction in transactions:
            item['deal_date'] = transaction.xpath('div[@class="address"]/div[@class="dealDate"]/text()').extract_first()
            if datetime.datetime.strptime(item['deal_date'],'%Y.%m.%d') < datetime.datetime.strptime('2020.10','%Y.%m'):
                break
            
            item['district'] = district
            title = transaction.xpath('div[@class="title"]/a/text()').extract_first()
            item['area'] = re.findall('\s.*?\s(.*?)平米',title)
            item['housing_estate'] = title.split()[0]
            item['total_price'] = transaction.xpath('div[@class="address"]/div[@class="totalPrice"]/span/text()').extract_first()
            item['unit_price'] = transaction.xpath('div[@class="flood"]/div[@class="unitPrice"]/span/text()').extract_first()
            yield item
        
        page_url = response.xpath('/html/body/div[5]/div[1]/div[5]/div[2]/div/@page-url').extract_first()
        page_data = response.xpath('/html/body/div[5]/div[1]/div[5]/div[2]/div/@page-data').extract_first()
        next_page = json.loads(page_data)['curPage']+1
        if next_page <= json.loads(page_data)['totalPage']:
            next_page_url = page_url.format(page = 1)
            yield scrapy.Request(response.urljoin(next_page_url))




