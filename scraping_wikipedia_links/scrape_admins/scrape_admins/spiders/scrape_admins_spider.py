from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
import re, time,unicodedata
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class scrape_admins_spider(BaseSpider):
    name = "scrape_admins"
    start_urls = ['https://en.wikipedia.org/w/index.php?title=Special:ListUsers/sysop&offset=&limit=9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999&group=sysop']

    def parse(self, response):
        global first_time_called
        hxs = HtmlXPathSelector(response)
        a = hxs.select('/html/body/div[3]/div[3]/div[3]/ul')
        admins = a.select('*//a[@class="mw-userlink"]//text()').extract()
        output = open("admins_list",'wb')
        for admin in admins:
            output.write(admin+'\n')
        output.close()
