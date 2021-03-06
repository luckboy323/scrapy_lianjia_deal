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

class SuningWareItem(Item):
	catentryId = Field()  # 物品ID
	catentdesc = Field()  # 物品名称
	price = Field()  # 价格
	praiseRate = Field()  # 好评率
	countOfarticle = Field()  # 评论数
	auxdescription = Field()  # 描述
	salesCode = Field()  # 销售码
	url = Field()  # 详情链接
	category = Field() # 类别
	ware = Field()  # 商品
	srcUrl = Field()

class ExpertItem(Item):
	nickname = Field() #姓名
	link = Field() #博文链接
	address = Field() #地址
	job = Field()  # 职业
	readers = Field() #阅读次数
	articlenum = Field() #文章数


class JdCategoryItem(Item):
	category1 = Field()  # 第一层类别
	category2 = Field()  # 第二层类别
	category3 = Field()  # 第三层类别
	path = Field()  # 类别路径
	searchKey = Field()  # 搜索关键字
	cid1 = Field()  # 第一层类别的ID
	cid2 = Field()  # 第二层类别的ID
	cid3 = Field()  #第三层类别的ID
	c3Url = Field()  #第三层类别的Url
	actionUrl = Field()


class JdWareItem(Item):
    wareId = Field()  # 商品ID
    wname = Field()  # 商品名称
    countOfarticle = Field()  # 评论总数
    price = Field()  # 商品价格
    selfsell = Field()  # 是否自营
    shopName = Field()  # 店铺名称
    praiseRate = Field()  # 好评率
    cid1 = Field()  # 第一层类别
    cid2 = Field()  # 第二层类别
    cid3 = Field()  # 第三层类别
    wareUrl = Field()