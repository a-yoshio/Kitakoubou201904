class Dog:
	def __init__(self,name,age,breed):
		self.name = name
		self.age = age
		self.breed = breed
	def showprofile(self):
		print("名前は",self.name,"です。",self.age,"歳です。","犬種は",self.breed,"です。")

dog3 = Dog("inu",5,"レトリバー")
dog3.showprofile()
