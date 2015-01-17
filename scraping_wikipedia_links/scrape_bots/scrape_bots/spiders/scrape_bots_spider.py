from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
import re, time,unicodedata
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class scrape_admins_spider(BaseSpider):
    name = "scrape_bots"
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:List_of_bots_by_number_of_edits']

    def parse(self, response):
        global first_time_called
        hxs = HtmlXPathSelector(response)

        a = hxs.select('/html/body/div[3]/div[3]/div[4]/table[3]')
        bots = a.select('*//td[2]//text()').extract()
        output = open("bots_list",'wb')
        bots.append('Helpful_Pixie_Bot')
        for bot in bots:
            output.write(bot+'\n')
        output.close()
