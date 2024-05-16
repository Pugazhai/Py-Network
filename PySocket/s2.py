import socket
from pickle import dumps,loads

x = socket.socket()
port, host = 5000,'127.0.0.1'

x.bind((host,port))
x.listen(5)
con, addr = x.accept()
print("connected Client",(con,addr))
data = con.recv(1024)
data = loads(data)
print("client sent data : ",data)
x.close()
