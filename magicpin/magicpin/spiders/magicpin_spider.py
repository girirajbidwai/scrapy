import scrapy
from scrapy_splash import SplashRequest
from ..items import MagicpinItem    

class magicpinSpider(scrapy.Spider):
    name = 'magicpin'
    def start_requests(self):
        url = 'https://magicpin.in/india/New-Delhi/All/Restaurant/'

        yield SplashRequest(url = url,callback = self.parse)

    def parse(self,response):
        all_article = response.css('div.cover-image-holder')

        print(len(all_article))
        items = MagicpinItem()
        for article in all_article:
            link = article.xpath("//a[@class='photo-link']/@href").extract()

            items['link'] = link
            yield items
            # break

        # for page in items['link']:
