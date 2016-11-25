# -*- coding: UTF-8 -*-

# 导入框架内置基本类class scrapy.spider.Spider
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider

# 导入爬取一般网站常用类class scrapy.contrib.spiders.CrawlSpider和规则类Rule
import chardet
from bs4 import BeautifulSoup
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request

from scrapy_demo.items import ExpertItem

# 设置编码格式
# reload(sys)
# sys.setdefaultencoding('utf-8')

add = 0
class CSDNPaperSpider(CrawlSpider):
    name = "csdn_expert_spider"
    allowed_domains = ["csdn.net"]
    page = 1
    Experts = []
    # 自定义规则
    #rules = [Rule(LxmlLinkExtractor(allow=('/peoplelist\.html?channelid=0&page=\d{,3}')), follow=True, callback='parseItem')]



    def start_requests(self):
        # 定义爬虫的入口网页
        start_urls = "http://blog.csdn.net/peoplelist.html?channelid=0&page=1"

        yield Request(url=start_urls, meta={"item": ExpertItem, "result": self.Experts}, callback=self.parseItem)  # 去爬关注人

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
        sites = soup.find_all('dl', "experts_list")
        for site in sites:
            item = ExpertItem()
            # 姓名、链接、地址、职业、阅读次数、文章数
            item['nickname'] = site.find('dd', "").a.get_text()
            item['link'] = site.find('dd', "").a.get('href')
            if site.find('div', "address").em:
                item['address'] = site.find('div', "address").em.get_text().encode('utf8')
            else:
                item['address'] = '无'
            item['job'] = site.find('div', "address").span.get_text().encode('utf8')
            item['articlenum'] = site.find('div', "count_l fl").b.get_text()
            item['readers'] = site.find('div', "count_l fr").b.get_text()

            add += 1
            yield item
            # self.Experts.append(item)
        print("The total number:",add)
        self.page += 1
        if self.page<108:
            urls = "http://blog.csdn.net/peoplelist.html?channelid=0&page=%d" % self.page
            yield Request(url=urls, meta={"item": ExpertItem, "result": self.Experts}, callback=self.parseItem)

            # return self.Experts

