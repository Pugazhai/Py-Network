# import socket
# from pickle import dumps,loads
# import threading

# # Server socket 
# def recv_from_client():
#     global con
#     while(connected):
#         data = con.recv(1024)
#         print("Receive from Client ",loads(data))

# x = socket.socket()
# port, host = 5000,'127.0.0.1'

# x.bind((host,port))
# x.listen(2)

# clients = []
# i = 0
# while i < 2:
#     con, addr = x.accept()
#     clients.append((conn,addr))
#     print("Client connected",addr)
#     i += 1




# con, addr = x.accept()
# connected = True
# t = threading.Thread(target=recv_from_client)
# t.start()
# print("Receiving Started")


import socket
import threading
from pickle import loads, dumps

def recv_from_clients(con,addr):
    while(connected):
        data = con.recv(1024)
        print(f'Received the Client {con,loads(data)}')

x= socket.socket()
port, host = 5000, '127.0.0.1'
x.bind((host,port))
x.listen(2)
clients = []
i = 0
while i < 2:
    con, addr = x.accept()
    clients.append((con,addr))
    print("Client connected",addr)
    i += 1
connected = True
active_threads = []
for x in clients:
    t = threading.Thread(target=recv_from_clients,args=x)
    t.start()
    active_threads.append(t)
