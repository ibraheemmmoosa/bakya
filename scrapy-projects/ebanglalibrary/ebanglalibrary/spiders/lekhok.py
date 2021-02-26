import scrapy


class LekhokSpider(scrapy.Spider):
    name = "lekhok"

    def start_requests(self):
        urls = ['https://www.ebanglalibrary.com/%E0%A6%B2%E0%A7%87%E0%A6%96%E0%A6%95-%E0%A6%B0%E0%A6%9A%E0%A6%A8%E0%A6%BE/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response)
        print(response.url)
        print(response.body)
        self.log('Got response!')
