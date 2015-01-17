# Scrapy settings for scrape_bots project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrape_bots'

SPIDER_MODULES = ['scrape_bots.spiders']
NEWSPIDER_MODULE = 'scrape_bots.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrape_bots (+http://www.yourdomain.com)'
