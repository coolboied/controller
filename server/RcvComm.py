import os
import threading
from socket import *
import queue
import select

class RcvMess(threading.Thread):
	def __init__(self, port, task_queue):
		threading.Thread.__init__(self)
		self.port = port
		self.socks = queue.Queue()
		HOST=''
		BUFSIZ=1024

		ADDR=(HOST, self.port)
		self.sock=socket(AF_INET, SOCK_STREAM)
		self.sock.bind(ADDR)
		self.cache={}
		self.task_queue = task_queue
	
	def rev_mess(self):
		self.sock.listen(50)
		infds,outfds,errfds = select.select([self.sock,],[],[],1)
		if len(infds) != 0:
			clientsock, clientaddr = self.sock.accept()
			self.socks.put(clientsock)
		if self.socks.qsize() != 0:
			try:
				clientsock = self.socks.get()
				print(clientsock.getsockname())
				buff = clientsock.recv(1024)
				self.deal_mess(buff.decode('utf-8'), clientsock)
				self.socks.put(clientsock)
			except Exception as e:
				print(e)

	def deal_mess(self, buff, sock):
		theDict = sock.getpeername()[0]+str(sock.getpeername()[1])
		theDict = theDict.replace('.','_')
		print(theDict)
		cache = ''
		try:
			cache = self.cache[theDict]
		except:
			print(self.cache)
			self.cache[theDict] =''
		buff = cache+buff
		comm_list = buff.split('#')
		if(buff[-1] != '#'):
			self.cache[theDict] = comm_list[-1]
			comm_list.pop(-1)
		else:
			self.cache[theDict]=''
		for comm in comm_list:
			self.task_queue.put({'command':comm, 'sock':sock})

	def run(self):
		while 1:
			self.rev_mess()

