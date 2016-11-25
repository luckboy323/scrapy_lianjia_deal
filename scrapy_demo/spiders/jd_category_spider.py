# -*- coding: UTF-8 -*-

import scrapy
import json
import time
from scrapy.http import Request
from scrapy_demo.items import JdCategoryItem



class LianjiaSpider(scrapy.Spider):
    print '------begin spider jd data-------'
    name = "jd_category_spider"
    allowed_domains = ["jd.com"]
    start_urls = [
        "http://so.m.jd.com/category/all.html"
    ]


    def parse(self, response):
        print '------jd_category_spider response-------'
        pos = response.body.find("jsArgs['category'] = ")
        print pos
        ary = response.body[pos+len("jsArgs['category'] = "):len(response.body)].split(';')
        str = ary[0]
        pos1=str.find("roorList : ")
        roorList = str[pos1+len("roorList : "):len(str)-1]
        categoryJson = json.loads(roorList)

        catalogUpdateTime = categoryJson['catalogUpdateTime']
        print catalogUpdateTime
        categoryList = categoryJson['catelogyList']
        for category in categoryList:
            level = category['level']
            category1 = category['name']
            cid1 = category['cid']
            categoryUrl = 'http://so.m.jd.com/category/list.action?_format_=json&catelogyId=%s' % cid1
            print "*****%s******%s*****%s*****" % (level,category1,cid1)
            yield Request(url=categoryUrl, meta={'category1':category1,'cid1':cid1}, callback=self.parseCategory)


    def parseCategory(self,response):
        print '------------parseCategory------------'
        category1 = response.meta['category1']
        cid1 = response.meta['cid1']
        bodyStr = response.body
        bodyStr = bodyStr.replace('\\','')
        pos = bodyStr.find('{"jshopUrl"')
        bodyJsonStr = bodyStr[pos:len(bodyStr)-2]
        bodyJson = json.loads(bodyJsonStr)
        datas = bodyJson['data']
        for data in datas:
            # tmp = data[0]
            if data.has_key('name'):
                category2 = data['name']
                print "**********"+category2
            catelogyList= data['catelogyList']
            for catelogy in catelogyList:
                item = JdCategoryItem()
                searchKey = ''
                path = ''
                if catelogy.has_key('path'):
                    path = catelogy['path']
                if catelogy.has_key('searchKey'):
                    searchKey = catelogy['searchKey']
                cid3 = catelogy['cid']
                category3 = catelogy['name']
                icon = catelogy['icon']

                item['category1'] = category1
                item['category2'] = category2
                item['category3'] = category3
                item['cid1'] = cid1
                item['cid3'] = cid3
                item['c3Url'] = response.url
                item['path'] = path
                item['searchKey'] = searchKey

                yield item
                # print '***%s***%s***%s***%s***%s' % (path,cid3,category3,icon,searchKey)

        time.sleep(1)
