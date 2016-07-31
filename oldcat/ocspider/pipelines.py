# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging

from ..models.news import News

logger = logging.getLogger(__name__)


class NewsPipeline(object):

    def process_item(self, item, spider):
        frm = item['url'].encode("utf-8", "ignore")
        title = item['title'].encode("utf-8", "ignore")
        article = item['content'].encode("utf-8", "ignore")
        update_time = item['created'].encode("utf-8", "ignore")
        news, created = News.get_or_create(frm=frm, defaults={
            "title": title,
            "article": article,
            "update_time": update_time,
        })
        logger.info("[created: %s] %s" % (created, news.frm))
