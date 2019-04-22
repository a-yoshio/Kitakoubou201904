class Exercise:
	def __init__(self,size,ch):
		self.size = size
		self.ch = ch
	def sankaku(self,size,ch):
		for i in range(1,size+1):
			print(ch*(i))

exersize = Exercise(5,"%")
exersize.sankaku(5,"%")
exersize.sankaku(3,"@")
exersize.sankaku(4,"&")
