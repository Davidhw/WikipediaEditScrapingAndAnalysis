from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
import re, time,unicodedata
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


good_links = []
global first_time_called 
first_time_called = True
class scrape_users_spider(BaseSpider):
    name = "scrape_users"
    start_urls = ['https://en.wikipedia.org/wiki/Wikipedia:List_of_Wikipedians_by_number_of_edits']

    def parse(self, response):
        global first_time_called
        hxs = HtmlXPathSelector(response)
#        a =  hxs.select('/html/body/div[3]/div[3]/div[4]')
#        users = a.select('//table[@class="wikitable"]//tr//td[2]//text()').extract()
        users = hxs.select('//tr[(((count(preceding-sibling::*) + 1) = 71) and parent::*)]//td[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//tr[(((count(preceding-sibling::*) + 1) = 22) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 2) and parent::*)] | //*[contains(concat( " ", @class, " " ), concat( " ", "wikitable", " " )) and (((count(preceding-sibling::*) + 1) = 27) and parent::*)]//td[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//tr[(((count(preceding-sibling::*) + 1) = 37) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//tr[(((count(preceding-sibling::*) + 1) = 63) and parent::*)]//tr[(((count(preceding-sibling::*) + 1) = 62) and parent::*)]//tr[(((count(preceding-sibling::*) + 1) = 8) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//tr[(((count(preceding-sibling::*) + 1) = 7) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "wikitable", " " )) and (((count(preceding-sibling::*) + 1) = 27) and parent::*)]//a//tr[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//a//tr[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "wikitable", " " )) and (((count(preceding-sibling::*) + 1) = 25) and parent::*)]//td[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "wikitable", " " )) and (((count(preceding-sibling::*) + 1) = 25) and parent::*)]//a//*[contains(concat( " ", @class, " " ), concat( " ", "wikitable", " " )) and (((count(preceding-sibling::*) + 1) = 25) and parent::*)]//a//text()').extract()

#        users = a.select('//table[@class="wikitable"]//tr//td//a//text()').extract()
#        users = a.select('/html/body/div[3]/div[3]/div[4]/table[6]//a//text()').extract()
#        users = hxs.select('/html/body/div[3]/div[3]/div[4]/table[6]//a//text()').extract()
        output = open("most_frequent_editors_list",'wb')
        for user in users:
            output.write(user+'\n')
        output.close()
