import scrapy

class LianjiaSpider(scrapy.Spider):
        name = "lianjia"
        allowed_domains = ["lianjia.com"]
        start_urls = [
            "http://tj.lianjia.com/ershoufang/rs%E5%9B%BD%E8%80%80%E4%B8%8A%E6%B2%B3%E5%9F%8E/"
        ]

        def parse(self, response):
            filename = response.url.split("/")[-2]
            with open(filename, 'wb') as f:
                f.write(response.body)
