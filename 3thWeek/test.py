# Run this script to get data results created with main.py

import sqlite3 as sql
from datetime import datetime

db = sql.connect("dataregex.db")
tableName = "data_" + str(datetime.today().strftime('%Y%m%d'))
query = """
SELECT * FROM %s""" %tableName
cur = db.cursor()
cur.execute(query)
print(cur.fetchall())
