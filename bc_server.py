from socket import *
while 1 :
    serverSock = socket(AF_INET, SOCK_STREAM)
    serverSock.bind(('192.168.0.21', 8080))
    serverSock.listen(1)

    connectionSock, addr = serverSock.accept()
    print(str(addr),' Connection verification complete.')

    data = connectionSock.recv(1024)
    print(data.decode('utf-8'))
    agree = input()

    if agree == 'y':
       energy = 100
       connectionSock.send('192.168.0.21'.encode('utf-8'))
       connectionSock.send(str(energy).encode('utf-8'))
       print('Transfer complete')
    else:
       print("You deny this deal")
