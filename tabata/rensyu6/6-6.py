class Exercize:
	def __init__(self,i):
		self.i = i

	def kuku(self,i):
		for j in range(1,10):
			print(i*j)

exercize = Exercize(5)
n = int(input())
exercize.kuku(n)
