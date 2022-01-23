# 2022 - YemekSepeti Python Web Development BootCamp

import sqlite3 as sql
import sys, json
from datetime import datetime
from user_model import User
from common import RE

if sys.argv[1] == "--file" and sys.argv[3] == "--db":
    try:
        path = sys.argv[2]
        dbName = sys.argv[4]
    except:
        print('Dosya okunamadı, geçerli bir dosya adı girin.')
if sys.argv[1] == "--db" and sys.argv[3] == "--file":
    try:
        dbName = sys.argv[2]
        path = sys.argv[4]
    except:
        print('Veritabanı bulunamadı, geçerli bir veritabanı adı girin.')

# Create table with date
tableName = "data_" + str(datetime.today().strftime('%Y%m%d'))

# Table columns
columns = """email, username, isimsoyisim, emailuserlk, usernamelk, 
             dogumyil, dogumay, dogumgun, ulke, ap"""

# Database connection
db = sql.connect(dbName)

# Creating table
createQuery = """CREATE TABLE IF NOT EXISTS %s (%s)""" %(tableName, columns)
cur = db.cursor()
cur.execute(createQuery)

# Read datas from json file
userList = []
with open(path) as jsonFile:
    jsonData = json.load(jsonFile)

# Prepare user data from json file
for data in jsonData:
    user = User()
    user.email = data["email"]
    user.username = data["username"]
    user.isimsoyisim = data["profile"]["name"]
    user.usernamelk = RE.verifyUsernamelk(user.username, user.email)
    user.emailuserlk = RE.verifyEmailuserlk(user.username, user.email)
    user.dogumyil = data["profile"]["dob"]
    user.dogumay = data["profile"]["dob"]
    user.dogumgun = data["profile"]["dob"]
    user.ulke = data["profile"]["location"]["lat"] + data["profile"]["location"]["long"]
    user.ap = "1"
    userList.append(user)

# Insert json datas into the table
for user in userList:
    insertQuery = f"""INSERT INTO {tableName} 
                    VALUES (
                            "{user.email}", 
                            "{user.username}", 
                            "{user.isimsoyisim}", 
                            "{user.usernamelk}", 
                            "{user.emailuserlk}", 
                            "{user.dogumyil}",
                            "{user.dogumay}", 
                            "{user.dogumgun}", 
                            "{user.ulke}",
                            "{user.ap}"
                    )"""
    cur.execute(insertQuery)
    db.commit()
db.close()