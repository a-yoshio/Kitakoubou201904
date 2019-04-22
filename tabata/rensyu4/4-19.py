sum = 0
c = 1
while True:
	n = int(input())
	if n == 0:
		c -= 1
		ave = sum/c
		print(ave)
		break
	else:
		sum += n
		c += 1

