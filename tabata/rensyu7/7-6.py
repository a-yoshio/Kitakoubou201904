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

	def get_count(self):
		result = y500en + y100en
		return result

	def get_amount(self,type):
		if type == 500:
			result = y500en * 500
			return result
		elif type == 100:
			result = y100en * 100
			return result

mycoin = CoinCase()
for i in range(4):
	type = int(input("硬貨の種類は？:\n"))
	count = int(input("硬貨の枚数は？\n"))
	mycoin.addcoins(type,count)

print("500円は",mycoin.getcount(500),"枚で",mycoin.get_amount(500),"円")
print("100円は",mycoin.getcount(100),"枚で",mycoin.get_amount(100),"円")
print("総枚数は",mycoin.get_count(),"枚")
print("総額は",mycoin.getamount(),"円")
