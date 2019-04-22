class Exercize:
	def __init__(self,n):
		self.n = n
	def prime(self,n):
		if n <= 3:
			return True
		for i in range(2,n):
			if n%i == 0:
				return False
		return True

exercize = Exercize(10100)

for j in range(10000,10100):
	if exercize.prime(j) == True:
		print(j)
