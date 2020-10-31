# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TransactionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    district = scrapy.Field()          # 区
    deal_date = scrapy.Field()         # 成交日期
    area = scrapy.Field()              # 面积
    unit_price = scrapy.Field()        # 每平方价格
    total_price = scrapy.Field()       # 总价
    housing_estate = scrapy.Field()    # 小区
    # houseInfo = scrapy.Field()         # 房屋信息
    # positionInfo = scrapy.Field()      # 位置与年份
    # deal_bg = scrapy.Field()             # 挂牌价与成交周期
    
