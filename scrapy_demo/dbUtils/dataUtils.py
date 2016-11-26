# -*- coding: UTF-8 -*-

from scrapy_demo.dbUtils.dbUtils import LightMysql

class DataUtils:

    def getDataFromMySQl(self):
        # 配置信息，其中host, port, user, passwd, db为必需
        dbconfig = {'host': 'localhost',
                    'port': 3306,
                    'user': 'root',
                    'passwd': 'root',
                    'db': 'spider',
                    'charset': 'utf8'}

        db = LightMysql(dbconfig)  # 创建LightMysql对象，若连接超时，会自动重连

        # 查找(select, show)都使用query()函数
        sql_select = "SELECT * FROM t_suning_category"
        result_all = db.query(sql_select)  # 返回全部数据
        # result_count = db.query(sql_select, 'count')  # 返回有多少行
        # result_one = db.query(sql_select, 'one')  # 返回一行
        list1 = []
        for result in result_all:
            url = result['wareUrl']

            fomart = '-0123456789'
            for c in url:
                if not c in fomart:
                    url = url.replace(c, '')
            ary = url.split('-')
            if len(ary) == 2:
                ci = url.split('-')[0]
                cf = url.split('-')[1]
                dict1 = {}
                dict1['category'] = result['category']
                dict1['ware'] = result['ware']
                dict1['ci'] = ci
                dict1['cf'] = cf
                list1.append(dict1)
        print "----list length is---%d" % len(list1)
        db.close()  # 操作结束，关闭对象
        return list1


    def getJdCategoryFromMySQl(self):
        # 配置信息，其中host, port, user, passwd, db为必需
        dbconfig = {'host': 'localhost',
                    'port': 3306,
                    'user': 'root',
                    'passwd': 'root',
                    'db': 'spider',
                    'charset': 'utf8'}

        db = LightMysql(dbconfig)  # 创建LightMysql对象，若连接超时，会自动重连

        # 查找(select, show)都使用query()函数
        sql_select = "SELECT * from t_jd_category WHERE cid2<>''"
        result_all = db.query(sql_select)  # 返回全部数据
        print "----list length is---%d" % len(result_all)
        db.close()  # 操作结束，关闭对象
        return result_all


    if __name__ == '__main__':
        # 配置信息，其中host, port, user, passwd, db为必需
        dbconfig = {'host': '192.168.100.239',
                    'port': 3306,
                    'user': 'devtest',
                    'passwd': 'devtest',
                    'db': 'Spider',
                    'charset': 'utf8'}

        db = LightMysql(dbconfig)  # 创建LightMysql对象，若连接超时，会自动重连

        # 查找(select, show)都使用query()函数
        sql_select = "SELECT * FROM t_suning_category"
        result_all = db.query(sql_select)  # 返回全部数据
        result_count = db.query(sql_select, 'count')  # 返回有多少行
        result_one = db.query(sql_select, 'one')  # 返回一行
        list1 = []
        for result in result_all:
            url = result['wareUrl']

            fomart = '-0123456789'
            for c in url:
                if not c in fomart:
                    url = url.replace(c, '')
            ary = url.split('-')
            if len(ary)==2:
                ci = url.split('-')[0]
                fi = url.split('-')[1]
                dict1 = {}
                dict1['category']=result['ware']
                dict1['ci']= ci
                dict1['fi'] = fi
                list1.append(dict1)
        print list1

        db.close()  # 操作结束，关闭对象
