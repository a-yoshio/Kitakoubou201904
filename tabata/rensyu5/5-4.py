s = 0
c = 0
numbers = []
while True:
	n = int(input())
	numbers.append(n)
	c += 1
	s += n
	if s > 10:
		for i in numbers:
			print(i)
		break
	elif c > 2:
		for j in numbers:
			print(j)
		break

	
