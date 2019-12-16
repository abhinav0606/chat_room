import sys
import socket
import select

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if len(sys.argv)!=3:
    print("connected striped and hello by")
    exit()
ip_adress=str(sys.argv[1])
port_number=int(sys.argv[2])
server.connect((ip_adress,port_number))
while True:
    listed=[sys.stdin,server]
    read,write,error=select.select(listed,[],[])
    for i in read:
        if i==server:
            message=i.recv(2048)
            print(message)
        else:
            message=sys.stdin.readline()
            server.send(b"{message}")
            sys.stdout.write("<you>")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()


