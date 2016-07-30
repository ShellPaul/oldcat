# -*- coding: utf-8 -*-

import re
import ast
import json
import logging
from urllib import quote

from lxml import etree
from scrapy import Spider
from scrapy.http import Request

from ..items import NewsItem

logger = logging.getLogger(__name__)


class NewsSpider(Spider):
    name = "news_spider"
    n360_time_hot = "https://www.so.com/?src=haosou.com"
    n360_th_pattern = re.compile(r"<script>var cardWatching=(.*?)</script>")
    toutiao_search = "http://toutiao.com/search_content/?offset=0&format=json&keyword={keyword}&autoload=true&count=50"
    toutiao_url_pattern = re.compile(r'href="(/group/\d+/)"')

    def __init__(self):
        self.download_delay = 1
        super(NewsSpider, self).__init__()

    def start_requests(self):
        yield Request(url=self.n360_time_hot, callback=self.parse_360_time_hot)

    def parse_360_time_hot(self, response):
        logger.info("parse 360 time hot: %s" % response.url)
        title_list = self.n360_th_pattern.findall(response.body)[0]
        title_list = ast.literal_eval(title_list)
        keywords = [ast.literal_eval("u'%s'" % block["keyword"]) for block in title_list]
        # logger.info("title list:\n%s" % json.dumps(keywords, indent=4))
        for keyword in keywords:
            url = self.toutiao_search.format(keyword=keyword.encode("utf-8"))
            yield Request(url, callback=self.parse_toutiao_search)

    def parse_toutiao_search(self, response):
        logger.info("parse toutiao search: %s" % response.url)
        pages = json.loads(response.body)['data']
        yield self.find_result(pages, 0)

    def find_result(self, pages, i):
        if i >= len(pages):
            return None
        page = pages[i]
        article_url = page['article_url']
        display_url = page['display_url']
        share_url = page['share_url']
        logger.info("pos [%d] of pages: <%s>" % (i, share_url))
        if not page['has_video'] and 'toutiao.com' in share_url:
            return Request(share_url, callback=self.parse_toutiao_page,
                           meta={'frm': article_url, 'pages': pages, 'pos': i})
        else:
            return self.find_result(pages, i+1)

    def parse_toutiao_page(self, response):
        if "toutiao.com" not in response.url:
            yield self.find_result(response.meta['pages'], response.meta['pos']+1)
            return
        logger.info("parse toutiao page: %s" % response.url)
        html = etree.HTML(response.body)
        item = NewsItem()
        item['url'] = response.meta['frm']
        item['title'] = html.xpath("//h1[@class='title']/text()")[0]
        item['created'] = html.xpath("//span[@class='time']/text()")[0]
        texts = html.xpath("//div[@class='article-content']//p/text()")
        texts = filter(None, (text.strip() for text in texts))
        imgs = html.xpath("//div[@class='article-content']//p/img/@src")
        imgs = map(response.urljoin, filter(None, (src.strip() for src in imgs)))
        item['content'] = json.dumps({"texts": texts, "imgs": imgs})
        # logger.info(json.dumps(dict(item), indent=4))
        yield item
