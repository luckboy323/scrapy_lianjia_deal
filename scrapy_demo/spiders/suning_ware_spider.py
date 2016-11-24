# -*- coding: UTF-8 -*-

import scrapy
from bs4 import BeautifulSoup
from scrapy_demo.items import SuningItem
from scrapy.http import Request
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
import time
from scrapy import log
import json

class LianjiaSpider(scrapy.Spider):
    name = "suning_ware_spider"
    log.msg('------ begin suning_ware_spider data-------', level=log.INFO, spider=name)
    Experts = []

    allowed_domains = ["suning.com"]
    start_urls = [
        "http://search.suning.com/emall/mobile/wap/clientSearch.jsonp?cityId=025&keyword=&channel=&cp=%d&ps=60&st=0&set=5&cf=0&iv=-1&ci=20006&ct=-1&channelId=WAP&sp=&sg=&sc=&prune=&operate=0&isAnalysised=0&istongma=1&v=99999999&callback=success_jsonpCallback" % page for page in range(1,10)
    ]
    domain='http://m.suning.com'

    def parse(self, response):
        print('------ response-------')
        wareString=response.body
        startPos= wareString.find('{"newArrivalsShown"')
        endPos=len(wareString)-2
        wareJsonStr = wareString[startPos:endPos]
        wareJson = json.loads(wareJsonStr)
        wares = wareJson['goods']

        for ware in wares:
             print ware['catentdesc']
             print ware['price']
             print ware['praiseRate']
             print ware['catentryId']
             print ware['countOfarticle']
             print ware['auxdescription']
             print ware['salesCode']
             print 'http://m.suning.com/product/%s/%s.html' % (ware['salesCode'],ware['catentryId'])


