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
        cb_kwargs = {
                'author': author,
                'biography': biography,
                }
        for writing_link in response.xpath('//div[@class="grid-wrapper"]/ol/li/a'):
            yield response.follow(writing_link, callback=self.parse_writing, cb_kwargs=cb_kwargs)

    def parse_writing(self, response, author=None, biography=None):
        title = response.xpath('//div/div[@class="site-content"]/div[@class="content-area"]/main[@class="site-main"]/header[@class="page-header"]/h1[@class="page-title"]/text()').get()
        description = response.xpath('//header/div[@class="taxonomy-description"]/p/text()').get()
        cb_kwargs = {
                'author': author,
                'biography': biography,
                'title': title,
                'description': description,
                }
        for section_link in response.xpath('//div[@class="grid-wrapper"]/article/div[@class="entry-inner"]/header[@class="entry-header"]/h2[@class="entry-title"]/a'):
            yield response.follow(section_link, callback=self.parse_sections, cb_kwargs=cb_kwargs)

    def parse_sections(self, response, author=None, biography=None, title=None, description=None):
        section_title = response.xpath('//div[@class="content-area"]/main[@class="site-main"]/article/header[@class="entry-header"]/h1[@class="entry-title"]/text()').get()
        section_content = response.xpath('//div[@class="content-area"]/main[@class="site-main"]/article/div[@class="entry-content"]/p/text()').getall()
        yield {
                'author': author,
                'biography': biography,
                'title': title,
                'description': description,
                'section_title': section_title,
                'section_content': section_content
                }
