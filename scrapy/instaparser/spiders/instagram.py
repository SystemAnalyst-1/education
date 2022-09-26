import scrapy
from scrapy.http import HtmlResponse


class InstaSpider(scrapy.Spider):
    name = 'gb'
    allowed_domains = ['scrapethissite.com']
    start_urls = ['https://www.scrapethissite.com/pages/advanced/?gotcha=csrf']


    def parse(self, response: HtmlResponse):
        csrf_token = response.xpath('//input[@name="csrf"]/@value').get()
        yield scrapy.FormRequest.from_response(
            response,
            formxpath="//form[@class ='form']",
            formdata={
                'csrf_token': csrf_token,
                'user': 'admin',
                'pass': 'admin'
            },
            callback = self.after_login
        )
    def after_login(self, response):
        quotes = response.xpath("//div[@class='row']//div//text()").get()
        print(f'Scrapy crawled {len(quotes)} quotes')



























