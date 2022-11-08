import time
from database2 import Database
import smbus

i2c = smbus.SMBus(1)
db=Database()

while(1):    
    luxBytes = i2c.read_i2c_block_data(0x48,0x10,2)
    Light = int.from_bytes(luxBytes, byteorder='big')
    print(Light)
    db.insert(Light)
    time.sleep(2)