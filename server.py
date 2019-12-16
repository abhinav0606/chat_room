import socket
import select
import sys
from _thread import *
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
if len(sys.argv)!=3:
    print("connected ,script,ipaddress,port_number")
    exit()
ip_adress=str(sys.argv[1])
port_number=int(sys.argv[2])
server.bind((ip_adress,port_number))
server.listen(100)
list_clients=[]
def clientthread(con,adr):
    con.send(b"welcome to the chat!")
    while True:
        try:
            message=con.recv(2048)
            if message:
                print("<"+adr[0]+">"+message)
                to_send="<"+adr[0]+">"+message
                broadcast(to_send,con)
            else:
                remove(con)
        except:
            continue
def broadcast(mes,connection):
    for i in list_clients:
        if i!=connection:
            try:
                i.send(mes)
            except:
                i.close()
                remove(i)
def remove(connection):
    if connection in list_clients:
        list_clients.remove(connection)
while True:
    conn,adrr=server.accept()
    list_clients.append(conn)
    print("connected"+adrr[0])
    start_new_thread(clientthread,(conn,adrr))
conn.close()
server.close()
