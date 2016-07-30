# -*- coding: utf-8 -*-

import string
import logging

# scrapy api
from scrapy import signals
from twisted.internet import reactor

from scrapy.crawler import Crawler, CrawlerProcess
from scrapy.settings import Settings

from ocspider import settings as settings_module
from ocspider.spiders.newsspider import NewsSpider

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    # python -m oldcat.spider_start

    settings_key_chars = string.uppercase + "_"
    settings_dict = {k: v
                     for k, v in vars(settings_module).items()
                     if all([(c in settings_key_chars) for c in k])}
    settings = Settings(settings_dict)

    crawler = CrawlerProcess(settings)
    crawler.crawl(NewsSpider)
    crawler.start()
