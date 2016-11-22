# -*- coding: UTF-8 -*-

import scrapy
from bs4 import BeautifulSoup
from scrapy_demo.items import LianJiaItem
from scrapy.http import Request
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
import time


add=0
page=0
class LianjiaSpider(scrapy.Spider):
    print '------begin spider suning data-------'
    Experts = []
    name = "suning_spider"
    allowed_domains = ["suning.com"]
    start_urls = [
        "http://m.suning.com/list/list.html"
    ]
    domain='http://m.suning.com'

    def parse(self, response):
        print '------suning_spider response-------'
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
                if cmp('http',wareUrl)>0:
                    wareUrl =  self.domain + wareUrl
                print "-----ware name is %s,url is %s" % (wareName,wareUrl)



        # global add
        # global page
        # soup = BeautifulSoup(response.body, "html5lib")
        # # 找到所有的博文代码模块
        # sites = soup.find('ul', "listContent").contents
        #
        # for site in sites:
        #     item = LianJiaItem()
        #     # 姓名、链接、地址、职业、阅读次数、文章数  houseName, houseType, area, dealTime, totalPrice, unitPrice, floor, memo
        #     title = site.find('div', "title").a.get_text()
        #     item['houseName'] = title.split(' ')[0].encode('utf8')
        #     item['houseType'] = title.split(' ')[1].encode('utf8')
        #     item['area'] = title.split(' ')[2].encode('utf8')
        #     item['dealTime'] = site.find('div', "dealDate").get_text().encode('utf8')
        #     item['totalPrice'] = site.find('div', "totalPrice").get_text().encode('utf8')
        #     item['unitPrice'] = site.find('div', "unitPrice").get_text().encode('utf8')
        #     item['floor'] = site.find('div', "positionInfo").get_text().encode('utf8')
        #     item['memo'] = site.find('div', "houseInfo").get_text().encode('utf8')
        #     add += 1
        #     print item['houseName']
        #     yield item
        # print("The total number:", add)
        #
        # page += 1
        # if page < 200:
        #     urls = "http://sz.lianjia.com/chengjiao/pg%d" % page
        #     yield Request(url=urls, meta={"item": LianJiaItem, "result": self.Experts}, callback=self.parse)
