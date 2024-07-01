import scrapy
from project_name.items import author

# from  project_name.items import Book
class ExampleSpider(scrapy.Spider):
    name = 'authors_crawler'
    start_urls = ['https://quotes.toscrape.com']
    #scrapy shell
    #scrapy crawl authors_crawler
    #scrapy startproject project_name

#css()=> return css object
#get() or getall() will return HTML string
#    

    def parse(self, response):
        domain  = self.start_urls[0]
        author_urls = response.css("div.quote span a::attr(href)").getall()
        for url in author_urls:
            yield response.follow(domain + url , callback = self.parse_author_detail )
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(domain + next_page,callback = self.parse)


        
    def parse_author_detail(self,response):
        auth = author()
        name = response.css("h3.author-title::text").get()
        born_date = response.css("span.author-born-date::text").get()
        born_location = response.css("span.author-born-location::text").get()
        description = response.css("div.author-description::text").get()
        auth['name'] = name
        auth['born_date'] = born_date
        auth['born_location'] = born_location
        auth['description'] = description
        yield auth
