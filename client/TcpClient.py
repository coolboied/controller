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
		mess = mess+'#'
		self.client.send(mess.encode('utf-8'))
	def recv_mess(self, length=1024):
		data = self.client.recv(length)
		return data
	def get_socket(self):
		return self.client

if __name__ == '__main__':
	tcpClient = TcpClient()
	while 1:
		tcpClient.send_mess(b'dir d:#')
		data = tcpClient.recv_mess()
		print(data.decode('utf-8'))
