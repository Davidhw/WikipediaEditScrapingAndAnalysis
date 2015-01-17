# Scrapy settings for scrape_contributions project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrape_contributions'

SPIDER_MODULES = ['scrape_contributions.spiders']
NEWSPIDER_MODULE = 'scrape_contributions.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrape_contributions (+http://www.yourdomain.com)'
