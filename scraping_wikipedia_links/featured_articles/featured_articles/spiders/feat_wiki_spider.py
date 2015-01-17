from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
import re,unicodedata,random

good_links = []
#from items import HpfanficItem
num_links = 100

class feat_wiki_spider(BaseSpider):
    name = "feat_wiki"
    start_urls = ['http://en.wikipedia.org/wiki/Wikipedia:Featured_articles']

    def parse(self, response):

        hxs = HtmlXPathSelector(response)
        generated_links = hxs.select('//@href').extract()
        for link in generated_links:
            if re.search(r'^/wiki/',link) and not re.search(r'/wiki/(Wikipedia:|Main_Page:|Special:|Portal|Help:|Category:|Lists_|List_of|:|User:|Wikipedia_talk:|Main_Page|File:|Template:)',link):
                good_links.append(link.encode('ascii','ignore'))
        output = open("wikipedia_featured_links",'wb')
        for link in random.sample(good_links,num_links):
            output.write('http://en.wikipedia.org'+link+'\n')
        output.close()
