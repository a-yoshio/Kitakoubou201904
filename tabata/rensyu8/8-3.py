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

cat1 = Cat()
dog1 = Dog()
cat1.showprofile("neko",6)
dog1.showprofile("wan",8)
cat1.sleep()
dog1.run()
cat1.speak()
dog1.speak()
