# -*- coding: UTF-8 -*-

import scrapy
from bs4 import BeautifulSoup
from scrapy_demo.items import SuningItem
from scrapy.http import Request
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
import time


class LianjiaSpider(scrapy.Spider):
    print '------begin suning_ware_spider data-------'
    Experts = []
    name = "suning_ware_spider"
    allowed_domains = ["suning.com"]
    start_urls = [
        "http://m.suning.com/list/20006-0.html"
    ]
    domain='http://m.suning.com'

    def parse(self, response):
        print '------suning_ware_spider response-------'
        lis = response.xpath('//ul[contains(@id, "productsList")]/li')

        for li in lis:
            wares = li.xpath('./a/div[2]/p[1]/text()').extract()[0]
            url = li.xpath('./a/@href').extract()[0]
            comments = li.xpath('./a/div[2]/div/p[2]/em[1]/i/text()').extract()
            if len(comments)>0:
                comment = comments[0]
            goodRates = li.xpath('./a/div[2]/div/p[2]/em[2]/i/text()').extract()
            if len(goodRates)>0:
                goodRate = goodRates[0]

            print "-----wares=%s--url=%s---comment=%s---goodRate=%s" % (wares,url,comment,goodRate)

                # item = SuningItem()
                # item['category'] = category[0]
                # item['ware'] = wareName
                # item['wareUrl'] = wareUrl
                # item['imgUrl'] = imgUrl
                # item['memo'] = ''
                # yield item

