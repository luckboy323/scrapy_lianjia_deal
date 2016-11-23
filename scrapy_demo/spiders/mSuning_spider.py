# -*- coding: UTF-8 -*-

import scrapy
from bs4 import BeautifulSoup
from scrapy_demo.items import SuningItem
from scrapy.http import Request
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
import time
from scrapy import log


class SuningSpider(scrapy.Spider):
    print '------begin spider suning data-------'
    Experts = []
    name = "suning_spider"
    allowed_domains = ["suning.com"]
    start_urls = [
        "http://m.suning.com/list/list.html"
    ]
    domain='http://m.suning.com'

    def parse(self, response):
        # print '------suning_spider response-------'
        log.msg('------suning_spider response-------',level=log.INFO,spider=self.name)
        lis = response.xpath('//div[contains(@id, "listItems")]/ul/li')

        for li in lis:
            titles = li.xpath('./em/text()').extract()
            print "-----titles="+titles[0]

        dls = response.xpath('//div[@class="list-detail hide"]/div/dl')
        for dl in dls:
            category = dl.xpath('./dt/text()').extract()
            if category[0]=='\n':
                category = dl.xpath('./dt/span/text()').extract()
            print "-----category=" + category[0]
            wareLis = dl.xpath('./dd/ul/li')
            for wareLi in wareLis:
                wareName = wareLi.xpath('./a/span/text()').extract()[0]
                wareUrl = wareLi.xpath('./a/@href').extract()[0]
                imgUrlList = wareLi.xpath('./a/img/@src').extract()
                if len(imgUrlList)>0:
                    imgUrl = imgUrlList[0]
                else:
                    imgUrl = ''
                if cmp('http',wareUrl)>0:
                    wareUrl =  self.domain + wareUrl
                print "-----ware name is %s,url is %s" % (wareName,wareUrl)
                item = SuningItem()
                item['category'] = category[0]
                item['ware'] = wareName
                item['wareUrl'] = wareUrl
                item['imgUrl'] = imgUrl
                item['memo'] = ''
                yield item

