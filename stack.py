

class Empty(Exception):
	pass

class StackArray(object):
	"""docstring for StackArray"""
	def __init__(self):
		self.data = []

	def __len__(self):
		return len(self.data)

	def __iter__(self):
		return self

	def next(self):
		try:
			top = self.top()
		except Empty:
			raise StopIteration()

		return self.pop()

	def is_empty(self):
		return len(self.data) == 0

	def push(self, obj):
		self.data.append(obj)

	def top(self):
		if self.is_empty():
			raise Empty("Stack is emmpty")

		return self.data[-1]

	def pop(self):
		if self.is_empty():
			raise Empty("Stack is emmpty")

		return self.data.pop()

stack = StackArray()

for x in range(10):
	stack.push(x)


for item in stack:
	print(item)