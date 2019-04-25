class Animal:
	def showprofile(self,name,age):
		print("名前は",name,"、",age,"歳です。")

	def speak(self):
		print(".....")

class Cat(Animal):
	def sleep(self):
		print("スースー")

	def speak(self):
		print("にゃー")

class Dog(Animal):
	def run(self):
		print("トコトコ")

	def speak(self):
		print("ワンワン")

animals = []
for i in range(4):
	if i %2 == 0:
		i=Cat()
		animals.append(i)
	else:
		i=Dog()
		animals.append(i)

for j in animals:
	j.speak()

