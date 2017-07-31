import abc
from time import gmtime, strftime


class WriteFile(object):
	def __init__(self, filename):
		self.filename=filename

	@abc.abstractmethod
	def write(self, text):
		"""writes the stuff in the file"""
		return


class LogFile(WriteFile):  

	def write(self,text):
		self.text=strftime("%Y-%m-%d %H:%M", gmtime()) + " " + text
		self.filename=open(self.filename, 'w')
		self.filename.write(self.text)
		self.filename.close()
		

class DelimFile (WriteFile):
	def write(self,text):
		self.text=','.join(text)
		self.filename=open(self.filename, 'w')
		self.filename.write(self.text)
		self.filename.close()
	pass

blog=LogFile('blog.txt')
blog.write("pierwszy log")
plik=DelimFile('plik.csv')
plik.write(['a','b','c','d'])
