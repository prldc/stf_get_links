# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class LinkbotSpider(scrapy.Spider):
    name = 'linkbot'
    allowed_domains = ['jurisprudencia.stf.jus.br']
    script = '''
               function main(splash, args)
                   assert(splash:go(args.url))
                   assert(splash:wait(5))
                   splash:set_viewport_full()
                   return splash:html()
                end
           '''

    def start_requests(self):
        yield SplashRequest(
            url="https://jurisprudencia.stf.jus.br/pages/search?base=acordaos&sinonimo=true&plural=true&page=1&pageSize=100&queryString=adi&sort=_score&sortBy=desc",
            callback=self.parse, endpoint="execute", args={
                'lua_source': self.script
            })

    def parse(self, response):
        current_page = response.xpath(".//li/a[@class='active']/span/text()").get()
        next_page = int(current_page) + 1
        out_dict = {}
        for processo in response.xpath(".//div[@class='result-container jud-text p-15 ng-star-inserted']"):
            link = processo.xpath(".//a[1]/@href").get()
            pdf_link = processo.xpath(".//div/div/a[@mattooltip = 'Inteiro teor']/@href").get()
            out_dict["nome"] = processo.xpath(".//a/h4/text()").get().strip()
            out_dict["link"] = f"https://jurisprudencia.stf.jus.br{link}"
            out_dict["pdf_link"] = pdf_link

            yield out_dict
        next_button = response.xpath(".//a[@class='pagination-icon']/span/i[@class='fa fa-angle-double-right']")
        if next_button:
            absolute_url = f"https://jurisprudencia.stf.jus.br/pages/search?base=acordaos&sinonimo=true&plural=true&page={next_page}&pageSize=100&queryString=adi&sort=_score&sortBy=desc"
            yield SplashRequest(url=absolute_url, callback=self.parse, endpoint="execute", args={
                'lua_source': self.script
            })
