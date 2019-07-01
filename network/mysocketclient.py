from socket import *

ip_port = ('127.0.0.1', 9999)
sockobj= socket(AF_INET, SOCK_STREAM)
sockobj.connect(ip_port)
sockobj.send("hello,server".encode('utf-8'))
server_reply=sockobj.recv(1024)
print(server_reply.decode("utf-8"))
sockobj.close()