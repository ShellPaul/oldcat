# -*- codingL utf-8 -*-

import peewee
from ..ocutils.db_connection import mysql


class News(peewee.Model):
    id = peewee.PrimaryKeyField()
    frm = peewee.CharField()
    title = peewee.CharField()
    article = peewee.CharField()
    keywords = peewee.CharField()
    update_time = peewee.DateTimeField()

    class Meta(object):
        database = mysql
        db_table = "news"


if __name__ == "__main__":
    News.create_table()
