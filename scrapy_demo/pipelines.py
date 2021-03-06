# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import json, codecs
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi
from scrapy import log

class ScrapyDemoPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWithEncodingCSDNPipeline(object):
    def __init__(self):
        self.file = codecs.open('papers.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        writeTime = json.dumps("日期："+str(item['writeTime']),ensure_ascii=False) + "\n"
        title = json.dumps("标题："+str(item['title']),ensure_ascii=False)+ "\n"
        link = json.dumps("链接："+str(item['link']),ensure_ascii=False)+ "\n"
        readers = json.dumps("阅读次数："+str(item['readers']),ensure_ascii=False)+ "\t"
        comments = json.dumps("评论数量："+str(item['comments']),ensure_ascii=False)+ "\n\n"
        line = writeTime + title + link + readers + comments
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

class MongoDBPipleline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("mongodb://jiwumdb:mdbjiwu@192.168.100.235:12000")
        db = clinet["Csdn"]
        self.Paper = db["expert"]

    def process_item(self, item, spider):
        """ 判断item的类型，并作相应的处理，再入数据库 """
        try:
            self.Paper.insert(dict(item))
        except Exception:
            pass
        return item

class MySQLPipleline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
        return cls(dbpool)

    # pipeline默认调用
    def process_item(self, item, spider):
        d = self.dbpool.runInteraction(self._do_upinsert, item, spider)
        d.addErrback(self._handle_error, item, spider)
        d.addBoth(lambda _: item)
        return d

    # 将每行更新或写入数据库中
    def _do_upinsert(self, conn, item, spider):
        if spider.name == 'lianjia_area_spider':
            print 'lianjia_area_spider'
            conn.execute("""
                               INSERT  INTO t_lianjia_deal (city, area, areaUrl,district,districtUrl,houseName, houseType, houseArea, dealTime, totalPrice, unitPrice, floor, memo)
                               VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)
                           """, (item['city'], item['area'], item['areaUrl'], item['district'], item['districtUrl'],item['houseName'], item['houseType'], item['houseArea'], item['dealTime'], item['totalPrice'], item['unitPrice'],
                           item['floor'], item['memo']))
            #self.insertAreaData(conn,item)
        elif spider.name == 'lianjia_deal_spider':
            print 'lianjia_deal_spider'
            self.insertDealData(conn, item)
        elif spider.name == 'suning_category_spider':
            print 'suning_spider'
            conn.execute("""
                               INSERT  INTO t_suning_category (category, ware, wareUrl,imgUrl,memo)
                               VALUES (%s, %s, %s, %s, %s)
                           """, (item['category'], item['ware'], item['wareUrl'], item['imgUrl'], item['memo']))
        elif spider.name == 'suning_ware_spider':
            print 'suning_ware_spider'
            conn.execute("""
                                             INSERT  INTO t_suning_ware (catentryId, catentdesc, price,salesCode,praiseRate,countOfarticle,auxdescription,url,category,ware,srcUrl)
                                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                         """, (
            item['catentryId'], item['catentdesc'], item['price'], item['salesCode'], item['praiseRate'],
            item['countOfarticle'], item['auxdescription'], item['url'], item['category'], item['ware'],item['srcUrl']))
        elif spider.name == 'csdn_expert_spider':
            conn.execute("""
                        INSERT  INTO t_csdn_expert (nickname, link, address, job, readers, articlenum)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (
            item['nickname'], item['link'], item['address'], item['job'], item['readers'], item['articlenum']))
        elif spider.name == 'jd_category_spider':
            conn.execute("""
                          INSERT  INTO t_jd_category (category1, category2, category3, cid1, cid2, cid3, c3Url, path, searchKey, actionUrl)
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                      """, (
                item['category1'], item['category2'], item['category3'], item['cid1'], item['cid2'], item['cid3'], item['c3Url'], item['path'], item['searchKey'], item['actionUrl']))
        elif spider.name == 'jd_ware_spider':
            conn.execute("""
                                        INSERT  INTO t_jd_ware (wareId, wname, countOfarticle, cid1, cid2, cid3, price, selfsell, shopName, praiseRate,wareUrl)
                                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                    """, (
                item['wareId'], item['wname'], item['countOfarticle'], item['cid1'], item['cid2'], item['cid3'],
                item['price'], item['selfsell'], item['shopName'], item['praiseRate'], item['wareUrl']))


        else:
            print 'not found the spider'


    def insertAreaData(conn,item):
        conn.execute("""
                   INSERT  INTO t_lianjia_area (city, area, areaUrl,district,districtUrl)
                   VALUES (%s, %s, %s, %s, %s)
               """, (item['city'], item['area'],item['areaUrl'], item['district'],item['districtUrl']))

    def insertDealData(conn,item):
        conn.execute("""
                   INSERT  INTO t_lianjia_deal (houseName, houseType, area, dealTime, totalPrice, unitPrice, floor, memo)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
               """, (
        item['houseName'], item['houseType'], item['area'], item['dealTime'], item['totalPrice'], item['unitPrice'],
        item['floor'], item['memo']))

    # 异常处理
    def _handle_error(self, failure, item, spider):
        log.err(failure)