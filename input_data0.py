import pandas as pd
import pymysql
import csv

def input_data (user_type, name): 
    db = pymysql.connect(host='localhost', port=3306, user='ems', passwd='emsqueen', db='test', charset='utf8')
    qr = 'select * from Expect'
    df = pd.read_sql(qr,db)
    if user_type == 'D':
        df.to_csv(r'/home/pi/Desktop/VPP/des_data/des_%s_data.csv'%name, index = False)
    else :
        df.to_csv(r'/home/pi/Desktop/VPP/consumer_data/consumer_%s_data.csv' %name, index = False)
    return 0

def add_list(user_type, name):
    
    if user_type == 'D':
        f_d = open('/home/pi/Desktop/VPP/des_data/des_list.csv', 'a')
        fd_d = pd.read_csv('/home/pi/Desktop/VPP/des_data/des_%s_data.csv'%name)
        wr_d = csv.writer(f_d)
        last_vd = fd_d.at[fd_d.index[-1],'Expect']
        wr_d.writerow([name,last_vd])
        print("Name: %s\nLast Expect: %d"%(name, last_vd))
        f_d.close()

    else :
        f_c = open('/home/pi/Desktop/VPP/consumer_data/consumer_list.csv', 'a')
        fd_c = pd.read_csv('/home/pi/Desktop/VPP/consumer_data/consumer_%s_data.csv' %name)
        wr_c = csv.writer(f_c)
        last_vc = fd_c.at[fd_c.index[-1],'Expect']
        wr_c.writerow([name,last_vc])
        print("Name: %s\nLast Expect: %d"%(name, last_vc))
        f_c.close() 
        
    return 0
        
        
cnt = 0

while  (cnt == 0):
    
    user_type = input("Enter 'D' for DES and 'C' for consumer : ")
    
    if (user_type == 'D' or user_type == 'C'):
        name = input("Enter your name : ")
        input_data(user_type, name)
        add_list(user_type, name)
        print("Your Data is saved.")
        break
    
    else:
        print("Check your typing.")