from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
import re, time,unicodedata


good_links = []
global first_time_called 
first_time_called = True
class reddit_wiki_spider(BaseSpider):
    name = "reddit_wiki"
    start_urls = ['http://www.reddit.com/r/wikipedia/top/?sort=top&t=all&limit=100']

    def parse(self, response):
        global first_time_called
        hxs = HtmlXPathSelector(response)
        generated_links = hxs.select('//p[@class="title"]/a//@href').extract()
        for link in generated_links:
            if re.search(r'ikipedia.org/wiki/',link) and not re.search(r'/wiki/(Wikipedia:|WP:|MediaWiki:|Main_Page:|Special:|Portal|Help:|Category:|Lists_|List_of|:|User:|Wikipedia_talk:|Main_Page|File:|Template:|User_talk|Talk)',link):
                good_links.append(link.encode('ascii','ignore'))
        if first_time_called:
            first_time_called = False
            next_url = hxs.select('//p[@class="nextprev"]/a[1]/@href').extract()[0].encode('ascii','ignore')
        else:
            try:
                next_url = hxs.select('//p[@class="nextprev"]/a[2]/@href').extract()[0].encode('ascii','ignore')
            except:
                next_url = None
        if next_url != None:
            print next_url
            time.sleep(2)
#            parse (next_url)
            yield Request(next_url,self.parse)
    
        output = open("wikipedia_subreddit_links",'wb')
        for link in good_links:
            output.write(link+'\n')
        output.close()
