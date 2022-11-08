import RPi.GPIO as GPIO
import time
import pandas as pd
import numpy as np
from heating_syster import Expect
from electricity import Expect2

global Expect, Expect2

pins = {'R':11, 'G':9, 'B':10}
cri = 1800
heating_cri = 300
electri_cri = 1500

consume = pd.read_csv('consumer1.csv')
mean = Expect+Expect2
print(mean)

GPIO.setmode(GPIO.BCM)          # GPIO BCM 모드 설정

for i in pins:
    GPIO.setup(pins[i], GPIO.OUT)
    GPIO.output(pins[i], GPIO.HIGH)

G = GPIO.PWM(pins['G'],2000)
B = GPIO.PWM(pins['B'],2000)
R = GPIO.PWM(pins['R'],2000)
    
R.start(0)
B.start(0)
G.start(0)

def map(x, in_min, in_max, out_min, out_max):
    return (x-in_min)*(out_max-out_min)/(in_max-in_min)+out_min
           
def Color(c):
    R_val = (c & 0x110000) >> 16
    R_val = map(R_val ,0,255,0,100)
    R.ChangeDutyCycle(100-R_val)

    B_val = (c & 0x000011)>>0
    B_val = map(B_val,0,255,0,100)
    B.ChangeDutyCycle(100-B_val)
 
    G_val = (c & 0x001100)>>8
    G_val = map(G_val,0,255,0,100)
    G.ChangeDutyCycle(100-G_val)

print("Power consumption reference : ", cri)
print("Heating sector power consumption reference : ", heating_cri)
print("Electric sector power consumption reference : ", electri_cri)
print("")
print("The expected amount of power used next month is ", mean)
print("Estimated heating power consumption is ", Expect)
print("Estimated electricity power consumption is ", Expect2)

if cri < mean:
    print("Please reduce the power usage !")
    if Expect > heating_cri:
        print("Reduce the use of heating power.")
    if Expect2 > electri_cri:
        print("Reduce the use of electricity power.")
        
    Color(0xFF0000)
    
elif cri > mean:
    print("You're keeping the standard power consumption.")
    Color(0x00FF00)
    
else:
    print("")
    Color(0xFF00FF)