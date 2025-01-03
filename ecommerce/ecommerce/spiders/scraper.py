import scrapy

class ScraperSpider(scrapy.Spider):
    name = "scraper"
    allowed_domains = ["www.scrapingcourse.com"]
    start_urls = ["https://www.scrapingcourse.com/ecommerce/"]

    def parse(self, response):
        products = response.css("li.product")
        for product in products:
             yield{
                'name':  product.css("h2::text").get(),
                'image_url': response.urljoin(product.css("img::attr(src)").get()),
                'price': "".join(product.css(".price *::text").getall()),
                'url': response.urljoin(product.css("a::attr(href)").get())
             }
