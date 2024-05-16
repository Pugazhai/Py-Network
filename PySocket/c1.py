import socket

x = socket.socket()
port,host = 5000,'127.0.0.1'
x.connect((host,port))
