import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DownloadZcoolItem

class ZcoolSpiderSpider(CrawlSpider):
    name = 'ZcOOL_spider'
    allowed_domains = ['zcool.com.cn']
    start_urls = ['https://www.zcool.com.cn/home?p=1']

    rules = (
        Rule(LinkExtractor(allow=r"https.+p=.+",unique=True), follow=True),
        Rule(LinkExtractor(allow=r'https://www.zcool.com.cn/work/.+=.html'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        image_urls = response.xpath('//div[contains(@class,"work-show-box")]//img//@src').extract()
        title = response.xpath('//div[contains(@class,"details-contitle-box")]//h2//text()').extract_first().strip() 
        item = DownloadZcoolItem(image_urls=image_urls, title=title)
        yield item