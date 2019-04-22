class Dog:
	def __init__(self,name):
		self.name = name
	def setname(self,name):
		print("名前は"+name+"です")
	
dog = Dog("inu")
dog.setname("inu")
