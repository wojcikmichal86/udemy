class MaxSizeList(object):
	def __init__(self, limit):
		self.limit=limit
		self.content=[]
	def push(self, item):
		self.item=item
		if len(self.content)<self.limit:
			self.content.append(self.item)
		else:
			self.content.remove(self.content[0])
			self.content.append(self.item)
	def get_list(self):
		return self.content

a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())
