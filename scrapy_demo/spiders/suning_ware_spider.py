# -*- coding: UTF-8 -*-
import scrapy
from scrapy_demo.items import SuningWareItem
import time
import json
from scrapy_demo.dbUtils.dataUtils import DataUtils


class LianjiaSpider(scrapy.Spider):
    name = "suning_ware_spider"
    print('------ begin suning_ware_spider data-------')
    Experts = []
    domain='http://m.suning.com'
    allowed_domains = ["suning.com"]
    dataUtils = DataUtils()
    resultList = dataUtils.getDataFromMySQl()
    # print resultList
    urlList = []
    for paramDict in resultList:
        # category = paramDict['category']
        # ware = paramDict['ware']
        cf = paramDict['cf']
        ci = paramDict['ci']
        for page in range(1, 101):
            start_url = "http://search.suning.com/emall/mobile/wap/clientSearch.jsonp?" \
                "cityId=755&keyword=&channel=&cp=%d&ps=60&st=0&set=5&cf=%s&iv=-1&ci=%s" \
                "&ct=-1&channelId=WAP&sp=&sg=&sc=&prune=&operate=0&isAnalysised=0&istongma=1" \
                "&v=99999999&callback=success_jsonpCallback" % (page,cf,ci)
            # print start_url
            urlList.append(start_url)
    print "----urlList length is---%d" % len(urlList)
    start_urls = urlList

    def parse(self, response):
        print('------ response-------')
        wareString=response.body
        # 解析url获取ci和cf，然后从获取resultList中获取category和ware
        wareurl = response.url
        warecf = wareurl.split('&')[7].split('=')[1]
        wareci = wareurl.split('&')[9].split('=')[1]
        for paramDict in self.resultList:
            if (paramDict['ci']==wareci and paramDict['cf']==warecf):
                category = paramDict['category']
                wareName = paramDict['ware']

        # 解析json字符串
        startPos= wareString.find('{"newArrivalsShown"')
        endPos=len(wareString)-2
        wareJsonStr = wareString[startPos:endPos]
        wareJson = json.loads(wareJsonStr)
        wares = wareJson['goods']
        for ware in wares:
            item = SuningWareItem()
            item['category'] = category
            item['ware'] = wareName
            item['srcUrl'] = wareurl
            item['catentdesc'] = ware['catentdesc']
            item['price'] = ware['price']
            item['praiseRate'] = ware['praiseRate']
            item['catentryId'] = ware['catentryId']
            item['countOfarticle'] = ware['countOfarticle']
            item['auxdescription'] = ware['auxdescription']
            item['salesCode'] = ware['salesCode']
            item['url'] = 'http://m.suning.com/product/%s/%s.html' % (ware['salesCode'],ware['catentryId'])
            yield item
        time.sleep(1)


