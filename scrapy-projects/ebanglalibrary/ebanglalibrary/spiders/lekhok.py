import scrapy


class LekhokSpider(scrapy.Spider):
    name = "lekhok"
    start_urls = ['https://www.ebanglalibrary.com/%E0%A6%B2%E0%A7%87%E0%A6%96%E0%A6%95-%E0%A6%B0%E0%A6%9A%E0%A6%A8%E0%A6%BE/']

    def parse(self, response):
        for author_link in response.xpath('//div[@id="writers-list"]/code/ul/li/a'):
            yield response.follow(author_link, callback=self.parse_author_writings_list)

    def parse_author_writings_list(self, response):
        author = response.xpath('//header/h1[@class="page-title"]/text()').get()
        biography = response.xpath('//header/div[@class="taxonomy-description"]/p/text()').get()
        writings = response.xpath('//div[@class="grid-wrapper"]/ol/li/a/text()').getall()
        yield {
                'author': author,
                'biography': biography,
                'writings': writings 
                }
