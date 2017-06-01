# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from mySpider.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowd_domains = ["jfz.com"]
    start_urls = [
        "http://www.jfz.com/simu/",
        "http://www.jfz.com/xintuo/"
    ]

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
    def parse(self, response):
        sel = scrapy.Selector(response)
        for h3 in response.xpath('//h3').extract():
            yield DmozItem(title=h3)

        for url in response.xpath('//a/@href').extract():
            yield DmozItem(link=url)
