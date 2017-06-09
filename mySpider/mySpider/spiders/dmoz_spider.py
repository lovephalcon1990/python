# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from mySpider.items import DmozItem
#from scrapy.spiders import CrawlSpider,Rule
#from scrapy.linkextractors import LinkExtractor

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowd_domains = ["mogujie.com"]
    start_urls = [
        "http://list.mogujie.com/book/clothing/50003",
    ]
    def parse(self,response):
        self.log('A response from %s just arrived!' % response.url)
        sel = scrapy.Selector(response)
        for h3 in response.xpath('//h3').extract():
            yield DmozItem(title=h3)

        for sel in response.xpath('//div[@class="goods_item"]'):
            self.log(sel)
#    rules = (
#        Rule(LinkExtractor(allow=('',),deny=('',))),
#        Rule(LinkExtractor(allow=('',)),callback='parse_item'),
#    )
#    def parse_item(self,response):
#        self.log('Hi, this is an item page! %s' % response.url)
        
    
#    def parse(self,response):
#       filename = response.url.split("/")[-2]
#       for sel in response.xpath('//ul/li'):
#            item = DmozItem()
#            item['title'] = sel.xpath('a/text()').extract()
#            item['link'] = sel.xpath('a/@href').extract()
#            item['desc'] = sel.xpath('img/text()').extract()
#            yield item
#    def start_requests(self):
#        return [scrapy.FormRequest("https://passport.coolyun.com/?appid=1010003&callback=http%3a%2f%2fbbs.coolpad.com%2flogin_sso_web.php",
#                                    formdata={'user': 'john', 'pass': 'secret'},callback=self.logged_in
#        )]
#
#    def loged_in(self,response):
#        
#        pass

#    def parse(self, response):
#        self.log('A response from %s just arrived!' % response.url)
#    def parse(self, response):
#        sel = scrapy.Selector(response)
#        for h3 in response.xpath('//title/text()').extract():
#            yield DmozItem(title=h3)
#
#        for url in response.xpath('//a/@href').extract():
#            if(not url):
#                continue
#            if(url.find('javascript') != -1):
#                continue
#            if(url.find('http') == -1):
#                request = response.url + url
#            else:   
#                continue
#            yield DmozItem(link=request)

#            yield scrapy.Request(request, callback=self.parse)
