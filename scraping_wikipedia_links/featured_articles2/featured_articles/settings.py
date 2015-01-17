# Scrapy settings for featured_articles project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'featured_articles'

SPIDER_MODULES = ['featured_articles.spiders']
NEWSPIDER_MODULE = 'featured_articles.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'featured_articles (+http://www.yourdomain.com)'
