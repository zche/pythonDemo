from socket import *

ip_port = ('0.0.0.0', 9999)
sockobj= socket(AF_INET, SOCK_STREAM)
sockobj.bind(ip_port)
sockobj.listen(128)
while True:
    connection,address = sockobj.accept()
    print("connect by:"+str(address))
    while True:
        data = connection.recv(1024)
        if not data:
            break
        decodeData='echo '+data.decode("utf-8")
        connection.send(decodeData.encode("utf-8"))
    connection.close()