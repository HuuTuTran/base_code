import scrapy
from minifigures.items import MinifiguresItem
# from myproject.items import Book
class ExampleSpider(scrapy.Spider):
    name = 'mini'
    start_urls = ['https://brixtoy.com/category/minifigures-collection/anime-cartoon-minifigures/anime/naruto-shippuden/']
    #scrapy shell
    #scrapy crawl example
    #scrapy startproject project_name

#css()=> return css object
#get() or getall() will return HTML string
#    

    def parse(self, response):
        figures_blocks = response.css("figure.product-media a")
        for row in figures_blocks:
            class_name = row.css("::attr(class)").get()
            if class_name != 'woocommerce-LoopProduct-link woocommerce-loop-product__link':
                continue
            detail_url = row.css("::attr(href)").get()
            yield response.follow(detail_url,callback = self.parse_detail_page)
        next_page_url  =  response.css("a.next::attr(href)").get()
        if next_page_url:
            yield response.follow(next_page_url,callback = self.parse)
    
    def parse_detail_page(self,response):
        mini = MinifiguresItem()
        mini['name'] = response.css("h1.product_title::text").get()
        mini['SKU'] = response.css("span.sku::text").get()
        mini['tag'] = response.css("span.tagged_as a::text").get()
        mini['price'] = response.css("bdi::text").get()
        mini['img_url'] = response.css("div.woocommerce-product-gallery__image::attr(data-thumb)").get()
        cates = ",".join(response.css("span.posted_in a::text").getall()) 
        mini['cates'] = cates
        yield mini
