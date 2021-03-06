# -*- codingL utf-8 -*-

import peewee
from ..ocutils.db_connection import mysql


class News(peewee.Model):
    id = peewee.PrimaryKeyField()
    frm = peewee.CharField(191, unique=True)
    title = peewee.CharField()
    article = peewee.CharField(51200)
    keywords = peewee.CharField(default="")
    update_time = peewee.DateTimeField()

    class Meta(object):
        database = mysql
        db_table = "news"


def hot_news(n=10):
    news = (News
            .select()
            .group_by(News.update_time.desc())
            .limit(n))
    return news


def all_news():
    return (News
            .select()
            .group_by(News.update_time.desc()))


if __name__ == "__main__":
    # python -m oldcat.models.news
    News.create_table()
