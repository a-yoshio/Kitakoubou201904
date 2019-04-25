class CoinCase:
	global y500en
	y500en = 0
	global y100en
	y100en = 0
	def addcoins(self,type,count):
		if type == 500:
			global y500en
			y500en += count
		elif type == 100:
			global y100en
			y100en += count

	def getcount(self,type):
		if type == 500:
			return y500en
		elif type == 100:
			return y100en

	def getamount(self):
		result = y500en * 500 + y100en * 100 
		return result

mycoin = CoinCase()
for i in range(4):
	type = int(input("硬貨の種類は？:\n"))
	count = int(input("硬貨の枚数は？\n"))
	mycoin.addcoins(type,count)

print("500円は",mycoin.getcount(500),"枚")
print("100円は",mycoin.getcount(100),"枚")
print("総額は",mycoin.getamount(),"円")
