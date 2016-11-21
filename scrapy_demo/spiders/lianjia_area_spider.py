# -*- coding: UTF-8 -*-

import scrapy
from scrapy_demo.items import LianJiaItem
from scrapy.http import Request



class LianjiaSpider(scrapy.Spider):
    print '------begin spider lianjia area data-------'
    name = "lianjia_area_spider"
    allowed_domains = ["lianjia.com"]

    global DOMAIN
    DOMAIN = "http://hz.lianjia.com/"
    global CITY
    CITY = "杭州"

    start_urls = [
        DOMAIN+"chengjiao/"
    ]


    def parse(self, response):
        print '------area response-------'

        areas =  response.xpath('//div[contains(@data-role, "ershoufang")]/div/a')
        for area in areas:
            areaUrl = area.xpath('@href').extract()[0]
            areaName = area.xpath('text()').extract()[0]
            urls = DOMAIN + areaUrl
            print "---areaUrl="+urls
            yield Request(url=urls, meta={}, callback=self.parseArea)


    def parseArea(self, response):
        print '------parseArea response-------'
        districts = response.xpath('//div[contains(@data-role, "ershoufang")]/div[2]/a')
        for district in districts:
            districtUrl = DOMAIN + district.xpath('@href').extract()[0]
            # districtName = district.xpath('text()').extract()[0]
            # print districtUrl
            # print districtName
            print "districtUrl=" + districtUrl
            yield Request(url=districtUrl, meta={}, callback=self.parseDistict)

            # total = response.xpath('//div[contains(@class, "total fl")]/span/text()').extract()[0]
            # pages = int(total)/30 +1
            # print '------district-------'+districtName+"-----%d" % pages
            # page = 1
            # while (page<=pages) and (page<=100):
            #     dealUrl = districtUrl + "pg%d/" % page
            #     yield Request(url=dealUrl, meta={}, callback=self.parseDeal)
            #     page += 1


    def parseDistict(self, response):
        # print '------parseDeal response-------'
        district = response.xpath('//div[contains(@data-role, "ershoufang")]/div[2]/a[@class="selected"]')
        districtUrl = DOMAIN + district.xpath('@href').extract()[0]
        districtName = district.xpath('text()').extract()[0]

        total = response.xpath('//div[contains(@class, "total fl")]/span/text()').extract()[0]
        pages = int(total) / 30 + 1
        print '------district-------' + districtName + "-----%d page----%s record" % (pages,total)

        page = 1
        while (page<=pages) and (page<=100):
            dealUrl = districtUrl + "pg%d/" % page
            print "dealUrl=" + dealUrl
            yield Request(url=dealUrl, meta={}, callback=self.parseDeal)
            page += 1

    def parseDeal(self, response):
        area = response.xpath('//div[contains(@data-role, "ershoufang")]/div[1]/a[@class="selected"]')
        areaName = area.xpath('text()').extract()[0]
        areaUrl = DOMAIN + area.xpath('@href').extract()[0]

        district = response.xpath('//div[contains(@data-role, "ershoufang")]/div[2]/a[@class="selected"]')
        districtUrl = DOMAIN + district.xpath('@href').extract()[0]
        districtName = district.xpath('text()').extract()[0]

        deals = response.xpath('//ul[contains(@class, "listContent")]/li')
        for deal in deals:
            item = LianJiaItem()
            item['city'] = CITY
            item['area'] = areaName
            item['areaUrl'] = areaUrl
            item['district'] = districtName
            item['districtUrl'] = districtUrl

            title = deal.xpath('./div/div[contains(@class,"title")]/a/text()').extract()[0]
            item['houseName'] = title.split(' ')[0]
            item['houseType'] = title.split(' ')[1]
            item['houseArea'] = title.split(' ')[2]
            item['dealTime'] = deal.xpath('./div/div[2]/div[2]/text()').extract()[0]
            totalPrice = deal.xpath('./div/div[2]/div[3]/span/text()').extract()[0]
            item['totalPrice'] = totalPrice + deal.xpath('./div/div[2]/div[3]/text()').extract()[0]
            unitPrice = deal.xpath('./div/div[3]/div[3]/span/text()').extract()[0]
            item['unitPrice'] = unitPrice + deal.xpath('./div/div[3]/div[3]/text()').extract()[0]
            item['floor'] = deal.xpath('./div/div[3]/div[1]/text()').extract()[0]
            item['memo'] = deal.xpath('./div/div[2]/div[1]/text()').extract()[0]
            yield item