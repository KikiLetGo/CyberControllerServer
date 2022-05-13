import socketserver
import socket

class CyberSocketServer(socketserver.BaseRequestHandler):	
	def handle(self):
		print("connection from",self.client_address)
		while True:
			data = self.request.recv(2048)
			if not data:
				break
			print('recv:', data)

class CyberSocket:
	def __init__(self):
		pass

	def start(self):
		hostname= socket.gethostname()#获取本地主机名
		sysinfo = socket.gethostbyname_ex(hostname)
		hostip=sysinfo[2][2]
		self.server = socketserver.ThreadingTCPServer((hostip, 2233), CyberSocketServer)
		print("server created")
		self.server.serve_forever()
	def send_data(self,data):
		request, client_address = self.server.get_request()
		data = data+"\n"
		print(data)
		request.sendall(data.encode())



