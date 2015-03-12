import os
import queue
import threading

class TaskThread(threading.Thread):
	def __init__(self, task_queue, req_queue):
		threading.Thread.__init__(self)
		print(1)
		self.task_queue = task_queue
		self.req_queue = req_queue
	
	def deal_task(self):
		while 1:
			try:
				print(3)
				task = self.task_queue.get()
				sock = task['sock']
				comm = task['command']
				print(comm)
				results = os.popen(comm).readlines()
				print(results)
				req = ''
				for result in results:
					req = req + result
				sock.send(req.encode('utf-8'))
			except Exception as e:
				print(e)
	
	def run(self):
		print('4')
		self.deal_task()


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
