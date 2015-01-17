from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
import re

first_time_called = True
good_links = []
class reddit_wiki_spider:

    name = 'reddit_wiki'
    start_urls = ['http://www.reddit.com/r/wikipedia/top/?sort=top&t=all&limit=100']

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        generated_links = hxs.select('//p[@class="title"]/a//@href').extract()
        for link in generated_links:
            if re.search(r'ikipedia.org/wiki/',link) and not re.search(r'/wiki/(Wikipedia:|Main_Page:|Special:|Portal|Help:|Category:|Lists_|List_of|:|User:|Wikipedia_talk:|Main_Page|File:|Template:)',link):
                good_links.append(link)
        if first_time_called:
            first_time_called = False
            next_url = hxs.select('//p[@class="nextprev"]/a[1]/@href').extract()
        else:
            next_url = hxs.select('//p[@class="nextprev"]/a[2]/@href').extract()
        if next_url != None:
            parse (next_url)
    
        output = open("wikipedia_subreddit_links",'wb')
        for link in good_links:
            output.write(link+'\n')
        output.close()
