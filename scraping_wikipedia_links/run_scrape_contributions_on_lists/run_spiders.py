import sys,random,re,os
from subprocess import call
inputfname = sys.argv[1]
#outputfname = sys.argv[2]
outputfname = "contributions_to_"+inputfname

def shellquote(s):
    return "'" +s.replace("'", "'\\''") + "'"
local_path = os.getcwd()

# import a list of wikipedia links
with open(inputfname) as input:
    links_list = input.readlines()

# make a sublist from random samplings of list
sublist = random.sample(links_list,10)


# make an output file pased on the name of the inported list
with open(outputfname, 'w+') as out:

    # for each link in sublist
    for link in sublist:
        # make link into page history
        topic = re.search(r'ikipedia.org/wiki/(.*)',link).group(1)
    # run scrape contributions on list and output file
#cd /home/d/Dropbox/scraping_wikipedia_links/scrape_contributions
        command = "scrapy crawl contributions -a start_url = "+'"'+"http://en.wikipedia.org/w/index.php?title="+topic+"&action=history&limit=999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999"+" -a output="+'"'+local_path+"/"+outputfname+'"'
        os.system("cd /home/d/Dropbox/scraping_wikipedia_links/scrape_contributions")
#        os.system(shellquote(command))

#        call (shellquote(command),shell=True)
#        call (["cd", "/home/d/Dropbox/scraping_wikipedia_links/scrape_contributions"])


        
