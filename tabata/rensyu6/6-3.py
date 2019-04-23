class Exersize:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def comparison(self,x,y):
		if x > y:
			return x
		else:
			return y

a = int(input())
b = int(input())
c = int(input())
exersize = Exersize(a,b)
print(exersize.comparison(a,exersize.comparison(c,b)))
