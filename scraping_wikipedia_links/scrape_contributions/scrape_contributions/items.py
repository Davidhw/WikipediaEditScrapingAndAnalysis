# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ScrapeContributionsItem(Item):
    author = Field()
    size = Field()
    # define the fields for your item here like:
    # name = Field()
    pass
