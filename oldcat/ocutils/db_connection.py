# -*- coding: utf-8 -*-

import os
import json
import peewee
from .dirs import etc_dir

db_json = os.path.join(etc_dir, "oldcat_db.json")

if not os.path.exists(db_json):
    with open(db_json, "w") as f:
        f.write(json.dumps({
            "user": "root",
            "password": "",
            "database": "oldcat",
            "host": "localhost",
            "port": 3306,
        }, indent=2))
    print "db file %s created, edit first!" % db_json
    exit(-1)

with open(db_json) as f:
    db_info = json.load(f)
mysql = peewee.MySQLDatabase(**db_info)
mysql.connect()
