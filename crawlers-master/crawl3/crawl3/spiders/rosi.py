# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from crawl3.items import ImageItem

# https://www.rosmm8.cc/

class RosiSpider(scrapy.Spider):
    name = "rosi"
    allowed_domains = ['www.rosmm.cc']
    start_urls = [
        'https://www.rosmm.cc',
    ]

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse,
                                    errback = self.errback,
                                    dont_filter = True)

    # 最重要的函数就是这个了
    def parse(self,  response):
        # yield self.parse_item(response) # ok
        for a in response.css('a::attr(href)').extract():
            if not a:
                continue
            next_page = response.urljoin(a)
            print "next_page:" + next_page
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_item(self, response):
        il = ItemLoader(item=ImageItem(), response=response)
        il.add_css('image_urls', 'img::attr(src)')
        return il.load_item()

    def errback(self, failure):
        pass

