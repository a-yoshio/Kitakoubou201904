class Exersize:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def comparison(self,x,y):
		if self.x > self.y:
			return self.x
		if self.y > self.x:
			return self.y

a = int(input())
b = int(input())
c = int(input())
exersize = Exersize(a,b)
print(exersize.comparison(exersize.comparison(a,b),c))
