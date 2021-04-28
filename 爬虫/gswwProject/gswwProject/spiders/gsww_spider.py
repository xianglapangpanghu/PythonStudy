import scrapy


class GswwSpiderSpider(scrapy.Spider):
    name = 'gsww_spider'
    allowed_domains = ['gushiwen.org']
    start_urls = ['http://gushiwen.org/']

    def parse(self, response):
        gsw_divs = response.xpath('//div[@class="left"]//div[@class="sons"]')
        # print(type(gsw_divs))
        for gsw_div in gsw_divs:
            title = gsw_div.xpath(".//b//text()")
            print(title)