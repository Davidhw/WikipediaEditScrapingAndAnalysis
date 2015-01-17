#import pdb

#pdb.set_trace()

import sys,random,re,os
from contributions_spider import *
inputfname = sys.argv[1]
#outputfname = sys.argv[2]
outputfname = "contributions_to_"+inputfname

local_path = os.getcwd()

# import a list of wikipedia links
with open(inputfname) as input:
    links_list = [x.strip() for x in input.readlines() if x.strip()]
    print links_list

# make a sublist from random samplings of list
#sublist = random.sample(links_list,10)


# make an output file pased on the name of the inported list
with open(outputfname, 'w+') as out:
    topics = []
    # for each link in sublist
    for link in links_list:
        # make link into page history
        try:
            topics.append(re.search(r'ikipedia.org/wiki/(.*)',link).group(1))
        except:
            print link
            print "ERROR, cannot apend link"
            sys.exit()

    links = []
    for topic in topics:
        links.append('http://en.wikipedia.org/w/index.php?title='+topic+'&action=history&limit=9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999')

    from twisted.internet import reactor
    from scrapy.crawler import Crawler
    from scrapy.settings import Settings
    
    print links
    spider = contributions_spider(start_urls = links,output = local_path+"/"+outputfname)

    crawler = Crawler(Settings())
    crawler.configure()
    crawler.crawl(spider)
    crawler.start()
    print "running spider"
    reactor.run()
    print "test"



        
