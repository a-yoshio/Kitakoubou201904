class Kitakobo:
	def __init__(self,number):
		self.number = number
	def square(self,number):
		self.result = number**2
		print(self.result)

kitakobo = Kitakobo(5)
kitakobo.square(6)

