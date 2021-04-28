import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import LywProjectItem


class LywSpiderSpider(CrawlSpider):
    name = 'lyw_spider'
    allowed_domains = ['lieyunwang.com']
    start_urls = ['https://www.lieyunwang.com/latest/p1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/latest/p\d+.html'), follow=True),
        Rule(LinkExtractor(allow=r'/archives/\d+'), callback="parse_detail", follow=False)
    )

    def parse_detail(self, response):
        title_list = response.xpath("//h1[@class='lyw-article-title-inner']/text()").getall()
        title = "".join(title_list).split()
        put_time = response.xpath("//h1[@class='lyw-article-title-inner']/span/text()").getall()
        author = response.xpath('//a[contains(@class,"author-name")]/text()').get()
        content = response.xpath('//div[@class="main-text"]').get()
        origin = response.url
        item = LywProjectItem(title=title, put_time=put_time, author=author, content=content, origin=origin)
        yield item
        # print("*"*30)
        # print(response.url)
        # print("*"*30)