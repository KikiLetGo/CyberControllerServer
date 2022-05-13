import socket
import threading
import json

class TcpServer:
    def __init__(self):
        self.port=2233#设置端口
        self.HEAD_LEN=8
        self.tcpServerSocket=socket.socket()#创建socket对象
        hostname= socket.gethostname()#获取本地主机名
        sysinfo = socket.gethostbyname_ex(hostname)
        hostip=sysinfo[2][2]
        self.tcpServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#让端口可以复用
        self.tcpServerSocket.bind((hostip,self.port))#将地址与套接字绑定，且套接字要求是从未被绑定过的
        self.tcpServerSocket.listen(5)#代办事件中排队等待connect的最大数目

    def set_receive_listener(self,receive_listener):
        self.receive_listener = receive_listener
    def server(self):
        while True:
            print("等待连接")
            self.clientSocket, addr = self.tcpServerSocket.accept()  
            print ('连接地址：', addr)
            if self.connected_listener:
                self.connected_listener()
            while True:
                try:
                    head_data=self.clientSocket.recv(self.HEAD_LEN)
                    if not len(head_data)==8:
                        print("bad package!head_data len:",head_data)
                        self.restart()
                        return
                    body_len = self.get_length_from_head_data(head_data)
                    body_data = self.clientSocket.recv(body_len)
                    if not body_len==len(body_data):
                        print("bad package!body_len:",body_len)
                        self.restart()
                        return
                    data_type = self.get_type_from_head_data(head_data)

                    if data_type == 1:#test/json data
                        text = body_data.decode()
                        print(text)
                        if not text:
                            break
                        if self.receive_listene