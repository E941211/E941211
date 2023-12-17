# 111年新竹市政府開課及參訓人次一覽表
# https://data.gov.tw/dataset/165354

import pymysql.cursors
import requests
import json

#GET API data
test = requests.get("https://odws.hccg.gov.tw/001/Upload/25/opendataback/9059/1548/4f151e9b-6f41-441f-9060-fe00940ba54f.json")
r = json.loads(test.text)

#Connect to the database
try:
    connection = pymysql.connect(host='localhost', 
                                 user='E94121151',       
                                 password='Fu20040109',
                                 database='wordpress',    
                                 cursorclass=pymysql.cursors.DictCursor)
         
except Exception as error:
    print(error)


with connection:
    with connection.cursor() as cursor:

        
        sql = "INSERT INTO `111年新竹市政府開課及參訓人次一覽表` (`課程類別`, `次數`, `時數`, `人次`,`學習時數`) VALUES (%s, %s, %s, %s, %s)"
        for i in range( len( r ) ):
            cursor.execute(sql, (r[i]['課程類別'],r[i]['次數'],r[i]['時數'],r[i]['人次'],r[i]['學習時數']))

    connection.commit()
    cursor.close()