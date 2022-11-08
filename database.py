# -*- coding: utf-8 -*-

import pymysql

class Database():
    def __init__(self):
        self.db = pymysql.connect(host='localhost',port=3306, user='ems',passwd='emsqueen',db='test',charset='utf8')
        self.cursor = self.db.cursor()
        
    def show(self):
        sql = "SELECT * FROM sensor"
        
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return(result);

    def insert(self,hum,temper):
        sql = "INSERT INTO sensor (humidity, temperature) VALUES (%s, %s)"
        self.cursor.execute(sql,(hum,temper))
        self.db.commit()
    
if __name__ == "__main__":
    db=Database();
    db.show();
