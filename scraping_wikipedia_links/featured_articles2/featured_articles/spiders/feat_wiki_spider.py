from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
import re, time,unicodedata

good_links = []
#from items import HpfanficItem


class feat_wiki_spider(BaseSpider):
    #name = "contributions"
    def __init__(self,start_url,output):
        
        name = "contributions"
        start_urls = [start_url]
        self.output_filename = output
        self.contribution_sizes = []
        self.users = []

    def parse(self, response):
        users = []
        page_history = hxs.select('//*[@id="pagehistory"]')

        user_histories = hxs.select('//*[@id="pagehistory"]//li//span[@class ="history-user"]').extract()

        for user_hist in user_histories:
            self.users.append(re.search(r'title="User:(.*)(" class| \(page does)',user_hist).group(1))
        self.contribution_sizes.append(page_history.re(r'mw-plusminus-[pos|neg|nul].*([\+|\-]\d+|\(0\))'))

        next_url_ending = hxs.select('/html/body/div[3]/div[3]/div[3]/a[9]/@href').extract()[0]
        if next_url_ending != None:
            next_url = 'en.wikipedia.org'+next_url_ending.encode('ascii','ignore')
            time.sleep(1)
            yield Request(next_url,self.parse)
    
        with open(self.output_filename,'a') as out:
            i = 0

        #[item for sublist in l for item in sublist]
            users_copy = users
            users = [user for sublist in users_copy for user in users_copy]

            contribution_sizes_copy = contribution_sizes_copy
            contribution_sizes = [size for sublist in contribution_sizes_copy for size in contribution_sizes_copy]

            for user in users:
                out.write(user+','+ self.contribution_sizes[i]+'\n')
                i+=1
