from cryptography.fernet import Fernet
from socket import *
import pymysql
import hashlib
from datetime import datetime
from database3 import Database

index = 0
db=Database()

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
    def hash_block(self):
        sha = hashlib.sha256()
        data = str(self.index) + str(self.timestamp) +  str(self.data) + str(self.previous_hash)
        sha.update(data.encode('utf-8'))
        return sha.hexdigest()

def create_genesis_block():
    return Block(0, datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = datetime.now()
    this_data = str(Energy_data)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

while 1:
    
    currency = input('How much do you want to spend ? ')
    value = bytes(currency,'utf-8')

    print("virtual currency : ", currency)

    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect(('192.168.0.21',8080))

    clientSock.send('Do you agree to send energy ? (y/n) '.encode('utf-8'))
    DES_server = clientSock.recv(1024)
    DES_energy_scale = clientSock.recv(1024)
    print('DES_server : ', DES_server.decode('utf-8'))
    print('DES_energy_scale : ', DES_energy_scale.decode('utf-8'))


    Energy_data = DES_energy_scale.decode('utf-8')
    print('Server connection complete.')


    if __name__ == '__main__':
        blockchain = [create_genesis_block()]
    previous_block = blockchain[0]


    index += 1
    for i in range(0, index):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        
        print(type(block_to_add.data), type(block_to_add.hash))
        print("Block #{} added blockchain".format(block_to_add.index))
        print("Energy Data: {}".format(block_to_add.data))
        print("Block Hash: {}n".format(block_to_add.hash))
        
    db.insert(block_to_add.index, block_to_add.data, block_to_add.hash) 
    
    #db = pymysql.connect(host='localhost', port=3306, user='ems', passwd='emsqueen', db='test', charset='utf8')