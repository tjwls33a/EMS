# -*- coding: utf-8 -*-

import Adafruit_DHT          
import time
from database import Database
sensor = Adafruit_DHT.DHT11 

pin = 4
db=Database()

while(1):
    h, t = Adafruit_DHT.read_retry(sensor, pin)

    if h is not None and t is not None :
        print("Temperature = {0:0.1f}*C Humidity = {1:0.1f}%".format(t, h))
        humi=(round(h,2))
        temper=(round(t,2))
        db.insert(humi,temper)
        time.sleep(1)

    else :
        print('Read error')
        time.sleep(2)

