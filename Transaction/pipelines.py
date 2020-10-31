# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pandas as pd
#from itemadapter import ItemAdapter


class TransactionPipeline:
    def process_item(self, item, spider):
        
        data=pd.DataFrame([item['district'], item['deal_date'],item['housing_estate'],item['area'],  item['unit_price'], \
                                                item['total_price']], 
                                                index=['district','deal_date','housing_estate', 
                                                        'area', 'unit_price','total_price']).T
        data.to_csv('cq_land.csv',index=False,encoding='gb2312')
        return item


class CqLandPipeline(object):        
    def process_item(self, item, spider):
        title=item['title']
        list_time=item['list_time']
        data=pd.DataFrame([title,list_time],index=['标题','推出时间']).T
        data.to_csv('cq_land.csv',index=False,encoding='gb2312')
        return item