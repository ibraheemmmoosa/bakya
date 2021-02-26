import scrapy


class LekhokSpider(scrapy.Spider):
    name = "lekhok"
    start_urls = ['https://www.ebanglalibrary.com/%E0%A6%B2%E0%A7%87%E0%A6%96%E0%A6%95-%E0%A6%B0%E0%A6%9A%E0%A6%A8%E0%A6%BE/']

    def parse(self, response):
        authors = []
        for author in response.xpath('//div[@id="writers-list"]/code/ul/li/a/text()').getall():
            authors.append(author)
            print(author)
        self.log('Got response!')
