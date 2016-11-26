# -*- coding: UTF-8 -*-
import scrapy
from scrapy_demo.items import JdWareItem
import time
import json
from scrapy_demo.dbUtils.dataUtils import DataUtils
from scrapy.http import Request

# 从苏宁的M站抓取数据：
# 1、首先获取分类列表：静态数据，获取回来直接用XPath解析即可
# 2、根据每个分类抓取相应的商品列表，翻页采用js动态加载，获取js的请求地址（返回json数据），解析Json
# 3、根据商品列表抓取详情页
class JdWareSpider(scrapy.Spider):
    name = "jd_ware_spider"
    print('------ begin jd_ware_spider data-------')
    Experts = []
    domain='http://m.jd.com'
    allowed_domains = ["jd.com"]
    dataUtils = DataUtils()
    resultList = dataUtils.getJdCategoryFromMySQl()
    # print resultList
    urlList = []
    for paramDict in resultList:
        c1 = paramDict['cid1']
        c2 = paramDict['cid2']
        c3 = paramDict['cid3']
        start_url = "http://so.m.jd.com/ware/searchList.action?_format_=json&stock=1&sort=&" \
                    "&page=1&categoryId=%s&c1=%s&c2=%s" % (c1, c2, c3)
        urlList.append(start_url)
    print "----urlList length is---%d" % len(urlList)
    start_urls = urlList

    def parse(self, response):
        print('------ response-------')
        wareString=response.body
        wareurl = response.url
        c1 = wareurl.split('&')[5].split('=')[1]
        c2 = wareurl.split('&')[6].split('=')[1]
        c3 = wareurl.split('&')[7].split('=')[1]
        # 解析json字符串
        wareString = wareString.replace('\\','')
        startPos= wareString.find('{"activityInfo"')
        endPos=len(wareString)-2
        wareJsonStr = wareString[startPos:endPos]
        wareJson = json.loads(wareJsonStr)
        wareCount = wareJson['wareCount']
        print wareCount

        warePage = wareCount/10 +1
        print warePage
        page = 1
        while page<warePage:
            start_url = "http://so.m.jd.com/ware/searchList.action?_format_=json&stock=1&sort=&" \
                        "&page=%d&categoryId=%s&c1=%s&c2=%s" % (page,c1,c2,c3)
            page += 1
            print start_url
            yield Request(url=start_url, meta={}, callback=self.parseWare)

    def parseWare(self,response):
        print('------parseWare response-------')
        wareString = response.body
        # 解析url获取ci和cf，然后从获取resultList中获取category和ware
        wareurl = response.url
        c1 = wareurl.split('&')[5].split('=')[1]
        c2 = wareurl.split('&')[6].split('=')[1]
        c3 = wareurl.split('&')[7].split('=')[1]

        # 解析json字符串
        wareString = wareString.replace('\\', '')
        startPos = wareString.find('{"activityInfo"')
        endPos = len(wareString) - 2
        wareJsonStr = wareString[startPos:endPos]
        wareJson = json.loads(wareJsonStr)
        wareCount = wareJson['wareCount']
        print wareCount
        wares = wareJson['wareList']
        for ware in wares:
            item = JdWareItem()
            item['wareId'] = ware['wareId']
            item['wname'] = ware['wname']
            item['countOfarticle'] = ware['totalCount']
            item['price'] = ware['jdPrice']
            item['selfsell'] = ware['self']
            item['praiseRate'] = ware['good']
            item['shopName'] = ware['shopName']
            item['cid1'] = c1
            item['cid2'] = c2
            item['cid3'] = c3
            item['wareUrl'] = 'http://item.m.jd.com/product/%s.html?sid=8bb24ee8ad6560f68320cd356f76f919' % ware[
                'wareId']
            yield item
        time.sleep(1)



