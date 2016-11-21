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
    print '------begin spider lianjia deal data-------'
    Experts = []
    name = "lianjia_deal_spider"
    allowed_domains = ["lianjia.com"]
    start_urls = [
        "http://sz.lianjia.com/chengjiao/pg2/"
    ]
    # 自定义规则
    # rules = [Rule(LxmlLinkExtractor(allow=('http://sz.lianjia.com/chengjiao/pg\d{,3}')), follow=True, callback='parse')]


    def parse(self, response):
        print '------response-------'
        # lis = response.xpath('//ul[contains(@class, "listContent")]/li')
        #
        # for li in lis:
        #     titles = li.xpath('./div/div[contains(@class,"title")]/a/text()').extract()
        #     print titles[0]

        global add
        global page
        soup = BeautifulSoup(response.body, "html5lib")
        # 找到所有的博文代码模块
        sites = soup.find('ul', "listContent").contents

        for site in sites:
            item = LianJiaItem()
            # 姓名、链接、地址、职业、阅读次数、文章数  houseName, houseType, area, dealTime, totalPrice, unitPrice, floor, memo
            title = site.find('div', "title").a.get_text()
            item['houseName'] = title.split(' ')[0].encode('utf8')
            item['houseType'] = title.split(' ')[1].encode('utf8')
            item['area'] = title.split(' ')[2].encode('utf8')
            item['dealTime'] = site.find('div', "dealDate").get_text().encode('utf8')
            item['totalPrice'] = site.find('div', "totalPrice").get_text().encode('utf8')
            item['unitPrice'] = site.find('div', "unitPrice").get_text().encode('utf8')
            item['floor'] = site.find('div', "positionInfo").get_text().encode('utf8')
            item['memo'] = site.find('div', "houseInfo").get_text().encode('utf8')
            add += 1
            print item['houseName']
            yield item
        print("The total number:", add)

        # nextpage = u'给自己的房子估价'
        # nextUrl = response.xpath(u"//button[text()='给自己的房子估价']/text()").extract()

        # nextPage = u'下一页'
        # nextUrl = response.xpath("//a[contains(text(),'%s')]/@href" % (nextPage)).extract()
        # print nextUrl[0]
        page += 1
        if page < 200:
            urls = "http://sz.lianjia.com/chengjiao/pg%d" % page
            yield Request(url=urls, meta={"item": LianJiaItem, "result": self.Experts}, callback=self.parse)
