from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
import re, time,unicodedata

num_links = 1000


good_links = []
global first_time_called 
first_timen_called = True
global links
links = []
class random_wiki_spider(BaseSpider):
    name = "rand_wiki"
    start_urls = ['https://en.wikipedia.org/wiki/Special:Random']

    def parse(self, response):
        global links
        print len(links)
        links.append(response.url)
        if len(links)<num_links:
            time.sleep(2)
            yield(Request('https://en.wikipedia.org/wiki/Special:Random', dont_filter=True, callback = self.parse))
        else:
            output = open("random_wikipedia_links",'wb')
            for link in links:
                output.write(link+'\n')
            output.close()
