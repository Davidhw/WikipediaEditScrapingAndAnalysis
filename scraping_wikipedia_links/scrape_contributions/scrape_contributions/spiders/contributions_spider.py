from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http.request import Request
import re, time,unicodedata
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

print "test 1"

global link_num
link_num =-1

class contributions_spider(BaseSpider):
    name = "contributions"


    def __init__(self, *args, **kwargs):
        super(contributions_spider, self).__init__(*args, **kwargs) 
        print "init of spider called"
#        name = "contributions"
        self.start_urls = kwargs.get('start_urls')
#        self.start_urls = [kwargs.get('start_url')] 
        self.output_filename = kwargs.get('output') 
        

    def parse(self, response):
        print "parse called"
        global link_num
        link_num+=1
        print link_num
        print "Parsing", response.url
        time.sleep(1)
        hxs = HtmlXPathSelector(response)
        page_history = hxs.select('//*[@id="pagehistory"]')

        contribution_sizes = []
        users = []
        
        users += hxs.select('//*[@id="pagehistory"]//li//span[@class ="history-user"]//a[1]//text()').extract()[0::2]
        print "appending users"

#        user_histories = hxs.select('//*[@id="pagehistory"]//li//span[@class ="history-user"]').extract()
#        for user_hist in user_histories:            
 #          search_relult = 2
            
#            search_result = re.search(r'title="User[:| ](.*)(?:" class="mw-userlink"|\(page does not exist\)|" href|action=)',user_hist)
#(r'title="User[:| ](.*)(" class="mw-userlink"|" href| \(page does)',user_hist)

#            if search_result !=None:
#                users.append(search_result.group(1))
 #           else:
  #              search_result = re.search(r'title="Special:Contributions/(\d[\d|\.]+)"',user_hist)
   #             if search_result !=None:
    #                users.append("IPADDRESS:"+search_result.group(1))
     #           else:
      #              search_result = re.search(r'title="User[:| ](.*)(\">.*</a>  <span)',user_hist)
       #             if search_result !=None:
        #                users.append(search_result.group(1))
         #           else:
          #              print "\n\n BOOM"
           #             print user_hist
        
        cs = page_history.re(r'mw-plusminus-[pos|neg|nul].*([\+|\-]\d+|\(0\))')
        for size in cs:
            if size =="(0)":
                size = "0"
            contribution_sizes.append(size)

        next_url_ending = hxs.select('/html/body/div[3]/div[3]/div[3]/a[@class="mw-nextlink"]/@href').extract()
        print "extracted"
#hxs.select('/html/body/div[3]/div[3]/div[3]/a[9]/@href').extract()
        
        print "next_url_ending is", next_url_ending
        if next_url_ending == []:
            print "done"
        else:
#            next_url = 'en.wikipedia.org'+next_url_ending.encode('ascii','ignore')
            next_url = 'http://en.wikipedia.org'+next_url_ending[0].encode('ascii','ignore')
            time.sleep(1)
            print "yielding next url"
            yield Request(next_url,self.parse)
    
        with open(self.output_filename,'a') as out:
            i = 0

        #[item for sublist in l for item in sublist]
            users_copy = users
#            users = [user for sublist in users_copy for user in users_copy]

#            contribution_sizes_copy = contribution_sizes
#            contribution_sizes = [size for sublist in contribution_sizes_copy for size in contribution_sizes_copy]

            for user in users:
#                print user
#                print users 
#                print "\n\nweeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee\n"
#                print contribution_sizes[0][i]
#                print type(contribution_sizes[0][i])
#                print contribution_sizes[0]
                try:
                    out.write(user+','+ contribution_sizes[i].encode('ascii','ignore')+'\n')
                except:
                    print "contribution_sizes:"
                    print contribution_sizes
                    print i
                    out.write(user+','+ 'ERROR'+'\n')
  #                  print "contrbiution_sizes[0]:"
   #                 print contribution_sizes[0]
    #                print i
 #                   pass
                    
                i+=1
            print "blarg"

                
