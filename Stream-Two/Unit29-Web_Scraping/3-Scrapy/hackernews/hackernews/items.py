from scrapy.item import Item, Field


class HackernewsItem(Item):
    """
    Define our Hackernews Item object
    """
    title = Field()
    url = Field()
