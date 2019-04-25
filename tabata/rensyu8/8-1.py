class Animal:
	def showprofile(self,name,age):
		print("名前は",name,"、",age,"歳です。")

class Cat(Animal):
	def sleep(self):
		print("スースー")

cat1 = Cat()
cat1.showprofile("neko",6)
cat1.sleep()
