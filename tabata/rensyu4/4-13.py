strike_count = 0
ball_count = 0
while True:
	n = int(input("ストライク=1 or ボール=2 ？"))
	if n == 1 :
		strike_count +=1
	elif n == 2 :
		ball_count +=1
	if strike_count == 3 or ball_count == 4:
		break
print("{0}ストライク,{1}ボール".format(strike_count,ball_count)) 

