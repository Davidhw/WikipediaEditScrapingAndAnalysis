# Scrapy settings for popular_articles project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'popular_articles'

SPIDER_MODULES = ['popular_articles.spiders']
NEWSPIDER_MODULE = 'popular_articles.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'popular_articles (+http://www.yourdomain.com)'
