# -*- coding: UTF-8 -*-

import scrapy, re, json, sys

# 导入框架内置基本类class scrapy.spider.Spider
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider

# 导入爬取一般网站常用类class scrapy.contrib.spiders.CrawlSpider和规则类Rule
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.http import Request
from bs4 import BeautifulSoup
from scrapy_demo.items import LianJiaItem
import chardet
import time


# 设置编码格式
# reload(sys)
# sys.setdefaultencoding('utf-8')

add = 0
class CSDNPaperSpider(CrawlSpider):
    name = "scrapy_demo"
    allowed_domains = ["sz.lianjia.com"]
    page = 1
    Experts = []
    # 自定义规则
    #rules = [Rule(LxmlLinkExtractor(allow=('/peoplelist\.html?channelid=0&page=\d{,3}')), follow=True, callback='parseItem')]
    louName = u"桐林公寓"


    def start_requests(self):
        # 定义爬虫的入口网页
        start_urls = "http://sz.lianjia.com/chengjiao/pg1rs"+self.louName
        #http://sz.lianjia.com/chengjiao/pg1
        yield Request(url=start_urls, meta={"item": LianJiaItem, "result": self.Experts}, callback=self.parseItem)  # 去爬关注人

    # 定义提取网页数据到Items中的实现函数
    def parseItem(self, response):
        global add
        data = response.body

        content_type = chardet.detect(data)
        if content_type['encoding'] != "UTF-8":
            data = data.decode(content_type['encoding'])
            data = data.encode("utf-8")

        soup = BeautifulSoup(data, "html5lib")
        # 找到所有的博文代码模块
        sites = soup.find('ul', "listContent").contents

        for site in sites:
            item = LianJiaItem()
            # 姓名、链接、地址、职业、阅读次数、文章数  houseName, houseType, area, dealTime, totalPrice, unitPrice, floor, memo
            title = site.find('div', "title").a.get_text()
            print(title.split(' ')[0])
            print(title.split(' ')[1])
            print(title.split(' ')[2])
            item['houseName'] = title.split(' ')[0]
            item['houseType'] = title.split(' ')[1]
            item['area'] = title.split(' ')[2]

            item['dealTime'] = site.find('div', "dealDate").get_text().encode('utf8')
            item['totalPrice'] = site.find('div', "totalPrice").get_text()
            item['unitPrice'] = site.find('div', "unitPrice").get_text()
            item['floor'] = site.find('div', "positionInfo").get_text()
            item['memo'] = site.find('div', "houseInfo").get_text()
            add += 1
            yield item
            # self.Experts.append(item)
        print("The total number:",add)
        self.page += 1
        if self.page<20:
            urls = "http://sz.lianjia.com/chengjiao/pg%drs" % self.page +self.louName
            #http://sz.lianjia.com/chengjiao/pg%d
            yield Request(url=urls, meta={"item": LianJiaItem, "result": self.Experts}, callback=self.parseItem)
            time.sleep(1)
            # return self.Experts

