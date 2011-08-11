#coding=utf-8
import re

from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from yeeyan.items import YeeyanItem

class YeeyanSpiderSpider(BaseSpider):
    name = 'yeeyan_spider'
    allowed_domains = ['yeeyan.org']
    start_urls = ["http://article.yeeyan.org/list_articles/410"]
    count = 0

    def parse(self, response):
        self.log("OK,%s"%response.url)
        hxs = HtmlXPathSelector(response)
        #将文章的链接继续进行处理
        divs = hxs.x('//div[@class="publicLeftCon mt10"]')
        for div in divs:
            url = div.x('h5/a/@href').extract()[0]
            yield self.make_requests_from_url(url).replace(callback=self.parse_content)
        #将下一页的链接继续进行处理
        next_url = hxs.x('//div[@id="project_left"]/div[@class="publicMiddleLine"]/span/a[b="下一页"]/@href').extract()[0]
        next_url = 'http://article.yeeyan.org'+next_url
        if self.count==2:
            return
        self.count+=1
        yield self.make_requests_from_url(next_url).replace(callback=self.parse)

    def parse_content(self, response):
        item = YeeyanItem()
        item['url'] = response.url
        hxs = HtmlXPathSelector(response)
        item['title'] = hxs.x('//title/text()').extract()[0]
        return item
