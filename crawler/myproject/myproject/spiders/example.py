import scrapy
from myproject.items import Book
class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['https://books.toscrape.com/index.html']
    #scrapy shell
    #scrapy crawl example
    #scrapy startproject project_name

#css()=> return css object
#get() or getall() will return HTML string
#    

    def parse(self, response):
        #response.css("span.text::attr(itemprop)").getall()
        #response.css("span.text").attrib['itemprop']


        spans = response.css("article.product_pod")
        for row in spans:
            title =  row.css("h3 a::attr(title)").get()
            price = row.css("p.price_color::text").get() 
            # print(title)
            # print(price)
            book = {'title':title,"price":price}

            detail_url = row.css("h3 a::attr(href)").get()
            detail_url="https://books.toscrape.com/"+ detail_url if 'catalogue' in detail_url else "https://books.toscrape.com/catalogue/" + detail_url
            yield response.follow(detail_url,callback=self.parse_book_detail,meta={"book_obj":book})

        # next_page = response.css("li.next a::attr(href)").get()
        # if next_page:
        #     next_page = "https://books.toscrape.com/"+ next_page if 'catalogue' in next_page else "https://books.toscrape.com/catalogue/" + next_page
        #     yield response.follow(next_page,callback=self.parse)
    def parse_book_detail(self,response):
        article = response.css("article.product_page p")
        # print(article[0].css("::text").get())
        for row in article:
            if not row.css("::attr(class)").get():
                book_obj = response.meta['book_obj']
                book_obj["descripion"] = row.css("::text").get()
                b= Book()
                b = book_obj
                yield b
