class Kitakobo:
	def square(self,number):
		self.result = number**2
		return int(self.result)

kitakobo = Kitakobo()
print(kitakobo.square(6))

