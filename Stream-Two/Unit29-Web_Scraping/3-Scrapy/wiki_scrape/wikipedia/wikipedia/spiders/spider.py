from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from wikipedia.items import WikipediaItem
from urlparse import urljoin


class WikipediaSpider(BaseSpider):

    name = "wiki"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = [
        "http://en.wikipedia.org/wiki/Category:2015_films"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.select('//div[@id="mw-pages"]//li')
        items = []

        for title in titles:
            item = WikipediaItem()
            url = title.select("a/@href").extract()

            if url:
                item["title"] = title.select("a/text()").extract()
                item["url"] = url[0]
                if "war" in str(item["title"]).lower():
                    item["url"] = urljoin("http://en.wikipedia.org", url[0])
                    items.append(item)
        return items
