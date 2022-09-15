import scrapy
from scrapy.http import HtmlResponse
from project_parser_hh.items import ProjectParserHhItem


class HhRuSpider(scrapy.Spider):

    name = 'hh_ru'
    allowed_domains = ['hh.ru']
    start_urls = [
        'https://spb.hh.ru/search/vacancy?area=76&search_field=name&search_field=company_name&search_field=description&text=python&no_magic=true&L_save_area=true&items_on_page=20',
        'https://spb.hh.ru/search/vacancy?area=88&search_field=name&search_field=company_name&search_field=description&text=python&no_magic=true&L_save_area=true&items_on_page=20'
    ]

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)

        urls_vacancies = response.xpath("//a[@data-qa='serp-item__title']/@href").getall()
        for url_vacancy in urls_vacancies:
            yield response.follow(url_vacancy, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        vacancy_name = response.css("h1::text").get()
        vacancy_salaries = response.xpath("//div[@data-qa='vacancy-salary']//text()").getall()
        vacancy_salary_to = ""
        vacancy_salary_from = ""
        if(len(vacancy_salaries)==1):
            vacancy_salary_to=vacancy_salaries[0]
            vacancy_salary_from = vacancy_salaries[0]
        else:
            for i in range(len(vacancy_salaries)):
                if vacancy_salaries[i] == ' до ':
                    vacancy_salary_to = vacancy_salaries[i+1]
                if vacancy_salaries[i] == 'от ':
                    vacancy_salary_from = vacancy_salaries[i+1]
        vacancy_url = response.url

        yield ProjectParserHhItem(
            name=vacancy_name,
            salary_from=vacancy_salary_from,
            salary_to=vacancy_salary_to,
            url=vacancy_url
        )
