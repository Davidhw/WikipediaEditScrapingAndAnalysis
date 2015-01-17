from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
import re,unicodedata

#from items import HpfanficItem
good_links = []
num_links = 100
class pop_wiki_spider(BaseSpider):
    name = "pop_wiki"
    start_urls = ['http://wikistics.falsikon.de/long/wikipedia/en/']

    def parse(self, response):
            hxs = HtmlXPathSelector(response)
            # generates many duplicates for some reason
            generated_links = hxs.select('//li').select('//@href').extract()
            for link in generated_links:
                if re.search(r'^http://en.wikipedia.org/wiki/',link) and not re.search(r'/wiki/(Wikipedia:|Main_Page:|Special:|Portal|Help:|Category:|Lists_|List_of|:|User:|Wikipedia_talk:|Main_Page|File:|Template:|404|Search|\%s|Talk)',link):
                    good_links.append(link.encode('ascii','ignore'))
            print len(good_links)
            with open("wikipedia_popular_links",'wb') as output:
                for link in good_links[:num_links]:
                    output.write(link+'\n')

