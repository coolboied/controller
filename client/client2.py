from socket import *

class TcpClient:
	HOST='127.0.0.1'
	PORT= 8000
	BUFSIZ=1024
	ADDR=(HOST, PORT)
	def __init__(self):
		self.client=socket(AF_INET, SOCK_STREAM)
		self.client.connect(self.ADDR)
	def send_mess(self, mess):
		self.client.send(mess)
	def recv_mess(self):
		data = self.client.recv(1024)
		return data


tcpClient = TcpClient()
i = 1
while 1:
	i+=1
	tcpClient.send_mess(b'dir e:#')
	if i%10 ==0:
		data = tcpClient.recv_mess()
		print(data.decode('utf-8'))
	
