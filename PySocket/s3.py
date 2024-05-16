import socket
from pickle import dumps,loads
import threading

# Server socket 
def recv_from_client():
    global con
    while(connected):
        data = con.recv(1024)
        print("Receive from Client ",loads(data))

x = socket.socket()
port, host = 5000,'127.0.0.1'

x.bind((host,port))
x.listen(5)

con, addr = x.accept()
connected = True
t = threading.Thread(target=recv_from_client)
t.start()
print("Receiving Started")
