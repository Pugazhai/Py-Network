import socket 
from pickle import dumps, loads
x = socket.socket()
port,host = 5000,'127.0.0.1'
x.connect((host,port))

ch = '1'
while(ch != '#'):
    print("Enter the data to send")
    data = input()
    x.sendall(dumps(data))
    