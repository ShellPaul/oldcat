# -*- coding: utf-8 -*-

import peewee

mysql = peewee.MySQLDatabase("oldcat", user="root")
mysql.connect()