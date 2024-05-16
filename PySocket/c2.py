import socket 
from pickle import dumps, loads
x = socket.socket()
port,host = 5000,'127.0.0.1'
x.connect((host,port))

# data = dumps("Hello this the new client")
data = dumps([x for x in "HelloWorld"])
print(data)
x.sendall(data)
# x.sendall(b"Hello this the new client")

