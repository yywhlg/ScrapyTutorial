import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor as sle
from tutorial.items import *
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


class LianjiaSpider(scrapy.Spider):
        name = "lianjia"
        allowed_domains = ["lianjia.com"]
        start_urls = [
            "http://tj.lianjia.com/ershoufang/pg2/"
        ]

        # response.css('.page-box .house-lst-page-box::attr(page-url)').extract()
        # response.css('.page-box .house-lst-page-box::attr(page-data)').extract()

        rules = (

            Rule(sle(allow=('http://tj.lianjia.com/ershoufang/pg\d+$')), callback='parse_item'),

            #  items = LinkExtractor(allow=('/ershoufang/pg2')).extract_links(response)
            #  for i in items:
            #       print i
            #

            # Rule(SgmlLinkExtractor(allow=('huhuuu/p/',)), callback='parse_item'),
            # Rule(SgmlLinkExtractor(allow=('huhuuu/archive/',)), callback='parse_item'),
        )

        # rules = [
        #     Rule(sle(allow=("/pg\d+$")), callback='parse', follow=True),
        # ]


        def parse(self, response):
            filename = response.url.split("/")[-2]
            with open(filename, 'wb') as f:
                f.write(response.body)


        # def parse(self, response):
        #     items = []
        #     sel = Selector(response)
        #     sites = sel.css('.info')
        #     for site in sites:
        #         item = TutorialItem()
        #         item['title'] = site.css('.info .title a::text').extract()
        #         items.append(item)
        #
        #         print item['title']
        #     return items

        def parse_item(self, response):
            items = []
            sel = Selector(response)
            sites = sel.css('.info')
            for site in sites:
                item = TutorialItem()
                item['title'] = site.css('.info .title a::text').extract()
                items.append(item)

                print item['title']
            return items