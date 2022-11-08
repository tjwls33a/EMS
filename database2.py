# -*- coding: utf-8 -*-

import pymysql

class Database():
    def __init__(self):
        self.db = pymysql.connect(host='localhost',port=3306, user='ems',passwd='emsqueen',db='test',charset='utf8')
        self.cursor = self.db.cursor()
        
    def show(self):
        sql = "SELECT Light FROM Light"   
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return(result);
    
    def show2(self):
        sql = "SELECT Light.Light, Expect.Expect FROM Light LEFT JOIN Expect ON Expect.num=Light.num"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return(result);

    def insert(self,Light):
        sql = "INSERT INTO Light (Light) VALUE (%s)"
        self.cursor.execute(sql,int(Light))
        self.db.commit()
        
    def insert2(self,Expect):
        sql = "INSERT INTO Expect (Expect) VALUE (%s)"
        self.cursor.execute(sql,Expect)
        self.db.commit()
    
if __name__ == "__main__":
    db=Database();
    db.show();
