# Scrapy settings for scrape_admins project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrape_admins'

SPIDER_MODULES = ['scrape_admins.spiders']
NEWSPIDER_MODULE = 'scrape_admins.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrape_admins (+http://www.yourdomain.com)'
