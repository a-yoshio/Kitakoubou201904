class Exersize:
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def average(self,x,y):
		self.result = int((x+y)/2)
		print(self.result)
exersize = Exersize(5,4)
exersize.average(10,11)
 
