from socketserver import TCPServer,BaseRequestHandler
import traceback
class MyBaseRequestHandler(BaseRequestHandler):
    '''
    #从BaseRequestHandler继承，并重写handle方法
    '''
    
    def handle(self):
        #循环监听读取来自客户端的数据
        while True:
            #当客户端主动断开连接时，self.recv(1024)会抛出异常
            try:
                #一次读取1024字节，并去除两端的空白字符
                data = self.request.recv(1024).strip()
                #self.client_address 是客户端连接(host,port)的元祖
                print("receive from (%r):%r" % (self.client_address,data.decode("utf-8")))
                #转换成大写后返回客户端
                self.request.sendall((data.decode("utf-8").upper()+"\n").encode("utf-8"))
            except:
                traceback.print_exc()
                break
if __name__ == "__main__":
    #telnet 127.0.0.1 9999
    ip_port = ('127.0.0.1', 9999)
    server=TCPServer(ip_port,MyBaseRequestHandler)
    #启动服务监听
    server.serve_forever()