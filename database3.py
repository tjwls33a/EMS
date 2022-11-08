import pymysql

class Database():
    def __init__(self):
        self.db = pymysql.connect(host='localhost',port=3306, user='ems',passwd='emsqueen',db='test',charset='utf8')
        self.cursor = self.db.cursor()
        
    def insert(self,index, energy, h):
        sql = "INSERT INTO BLOCK (Index_, Energy, Hash_) VALUE (%s, %s, %s)"
        self.cursor.execute(sql,(int(index), energy, h))
        self.db.commit()
        
    def show(self):
        sql = "SELECT * FROM BLOCK"   
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return(result);

    
if __name__ == "__main__":
    db=Database();
    db.show();