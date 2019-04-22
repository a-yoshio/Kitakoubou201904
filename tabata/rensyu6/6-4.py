class Exersize:
	def __init__(self,size):
		self.size = size

	def sankaku(self,size):
		for i in range(1,size+1):
			print("$"*(i))

exersize = Exersize(1)
exersize.sankaku(3)
exersize.sankaku(4)
exersize.sankaku(5)


