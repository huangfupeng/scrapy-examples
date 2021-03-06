# coding=utf-8
import re
import json


from scrapy.selector import Selector
import time

try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle


from doubanbook.items import *
from misc.log import *


class DoubanBookSpider(CrawlSpider):
    name = "doubanbook"
    allowed_domains = ["douban.com"]
    start_urls = [
        "http://book.douban.com/tag/"
    ]
    rules = [
        Rule(sle(allow=("/subject/\d+/?$")), callback='parse_2'),
        Rule(sle(allow=("/tag/[^/]+/?$", )), follow=True),
        Rule(sle(allow=("/tag/$", )), follow=True),
    ]

    def test_print(self, content="debug", path='/tmp/test.log'):
            fsock = open(path, 'a')
            now = time.strftime("%Y-%m-%d %H %M %S", time.localtime())
            result = '%s--%s\n' % (now, content)
            fsock.write(result)
            fsock.close()
            return result

    def parse_2(self, response):
        self.test_print(response)
        items = []
        sel = Selector(response)
        self.test_print(sel)
        sites = sel.css('#wrapper')
        for site in sites:
            item = DoubanSubjectItem()
            # extract(): 为了提取真实的原文数据
            item['title'] = site.css('h1 span::text').extract()
            item['link'] = response.url
            item['content_intro'] = site.css('#link-report .intro p::text').extract()
            items.append(item)
            # print repr(item).decode("unicode-escape") + '\n'
            print item
        # info('parsed ' + str(response))
        return items

    def parse_1(self, response):
        # url cannot encode to Chinese easily.. XXX
        info('parsed ' + str(response))

    def _process_request(self, request):
        info('process ' + str(request))
        return request
