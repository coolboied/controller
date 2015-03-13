import os
import queue
from RcvComm import *
from TaskThreadPool import *

class Server:
	def __init__(self):
		self.task_queue = queue.Queue();
		self.req_queue = queue.Queue();
		self.rcv_mess_thread = RcvMess(8000, self.task_queue)
	
	def start_recv_commander(self):
		self.rcv_mess_thread.start()
	def deal_commander(self):
		task_tread_pool = TaskTreadPool(self.task_queue, self.req_queue)
		task_tread_pool.create_threads(10)

server = Server()
server.start_recv_commander()
server.deal_commander()
