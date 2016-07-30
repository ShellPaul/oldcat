# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from ..models.news import News


class NewsPipeline(object):

    def process_item(self, item, spider):
        news = News()
        news.frm = item['url'].encode("utf-8", "ignore")
        news.title = item['title'].encode("utf-8", "ignore")
        news.article = item['content'].encode("utf-8", "ignore")
        news.update_time = item['created'].encode("utf-8", "ignore")
        news.save()