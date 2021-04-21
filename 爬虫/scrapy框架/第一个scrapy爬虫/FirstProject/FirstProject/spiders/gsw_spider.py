import scrapy
from ..items import FirstprojectItem

class GswSpiderSpider(scrapy.Spider):
    name = 'gsw_spider'
    allowed_domains = ['gushiwen.org']
    start_urls = ['https://www.gushiwen.cn/default_1.aspx']

    def myprint(self, value):
        print("↓"*40)
        print(value)
        print("↑"*40)
        print(" ")

    def parse(self, response):
        gsw_divs = response.xpath('//div[@class="left"]//div[@class="sons"and not(@style=" padding-bottom:12px;")]')
        for gsw_div in gsw_divs:
            title = gsw_div.xpath('.//b/text()').get()
            source = gsw_div.xpath('.//p[@class="source"]/a/text()').getall()
            author = source[0]
            dynasty = source[1]
            content_list = gsw_div.xpath('.//div[@class="contson"]//text()').getall()
            content = "".join(content_list).strip()
            # self.myprint(content)
            item = FirstprojectItem(title=title, author=author, dynasty=dynasty, content=content)
            yield item
