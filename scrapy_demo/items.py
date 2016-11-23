# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field

class ScrapyDemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class LianJiaAreaItem(Item):
	city = Field() #城市
	area = Field()  # 区域
	areaUrl = Field()  # 区域连接
	district = Field()  # 商圈
	districtUrl = Field()  # 商圈链接


class LianJiaItem(Item):
	city = Field()  # 城市
	area = Field()  # 区域
	areaUrl = Field()  # 区域连接
	district = Field()  # 商圈
	districtUrl = Field()  # 商圈链接
	houseName = Field() #房源名称
	houseType = Field()  # 户型
	houseArea = Field()  # 面积
	dealTime = Field()  # 成交时间
	totalPrice = Field()  #成交总价
	unitPrice = Field()  #成交单价
	floor = Field()  #楼层信息
	memo = Field()  #其他信息


class SuningItem(Item):
	category = Field()  # 类别
	ware = Field()  # 名称
	wareUrl = Field()  # 连接
	imgUrl = Field()  # 图片链接
	memo = Field()  #其他信息