class Dog:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def showprofile(self,name,age):
		print("名前は",name,"です。",age,"歳です。")

dog1 = Dog("inu",2)
dog2 = Dog("wan",5)
dog1.showprofile("inu",2)
dog2.showprofile("wan",5)
