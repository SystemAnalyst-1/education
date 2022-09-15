import scrapy
from scrapy.http import HtmlResponse
from project_parser_hh.items import ProjectParserHhItem


class SuperjobRuSpider(scrapy.Spider):
    name = 'superjob_ru'
    allowed_domains = ['superjob.ru']
    start_urls = [
        'https://www.superjob.ru/vacancy/search/?keywords=python&geo%5Bt%5D%5B0%5D=4',
        'https://tverskaya-oblast.superjob.ru/vacancy/search/?keywords=python'
    ]

    def parse(self, response: HtmlResponse):
        next_page = response.xpath("//a[@class='_1IHWd _6Nb0L _37aW8 _1Sycm f-test-button-dalshe f-test-link-Dalshe']/@href").get()

        if next_page:
            yield response.follow(next_page, callback=self.parse)

        urls_vacancies = response.xpath("//span[@class='_9fIP1 _249GZ _1jb_5 QLdOc']//a/@href").getall()
        for url_vacancy in urls_vacancies:
            yield response.follow(url_vacancy, callback=self.vacancy_parse)

    def vacancy_parse(self, response: HtmlResponse):
        vacancy_name = response.css("h1::text").get()
        vacancy_salaries = response.xpath("//span[@class='_2eYAG _1nqY_ _249GZ _1dIgi']//text()").getall()
        vacancy_salary_to = ""
        vacancy_salary_from = ""
        count = 0
        if (len(vacancy_salaries) == 1):
            vacancy_salary_to = vacancy_salaries[0]
            vacancy_salary_from = vacancy_salaries[0]
        else:
            for i in range(len(vacancy_salaries)):
                a = str(vacancy_salaries[i]).replace('\xa0', '')
                if vacancy_salaries[i] == 'до':
                    vacancy_salary_to = vacancy_salaries[i + 2]
                    count += 5
                elif vacancy_salaries[i] == 'от':
                    vacancy_salary_from = vacancy_salaries[i + 2]
                    count += 5
                elif a.isdigit():
                    if(count == 0):
                        vacancy_salary_to = vacancy_salaries[i]
                        count+=1
                    elif(count == 1):
                        vacancy_salary_from = vacancy_salaries[i]
        vacancy_url = response.url

        yield ProjectParserHhItem(
            name=vacancy_name,
            salary_from=vacancy_salary_from,
            salary_to=vacancy_salary_to,
            url=vacancy_url
        )