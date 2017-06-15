# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


#class MyspiderItem(scrapy.Item):
#    # define the fields for your item here like:
#    # name = scrapy.Field()
#    pass

class DmozItem(scrapy.Item):
    _id = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    orgPrice = scrapy.Field()
    price = scrapy.Field()
    image_urls = scrapy.Field()
    images  = scrapy.Field()
    sale = scrapy.Field()
