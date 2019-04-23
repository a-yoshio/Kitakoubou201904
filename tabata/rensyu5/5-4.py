s = 0
c = 0
numbers = []
while True:
	n = int(input())
	numbers.append(n)
	c += 1
	s += n
	if s > 99:
		for i in numbers:
			print(i)
		break
	elif c > 9:
		for j in numbers:
			print(j)
		break

	
