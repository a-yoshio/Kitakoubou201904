c = 0
numbers = []
while c < 5:
	n = int(input())
	numbers.append(n)
	c += 1
numbers.sort()
for i in numbers:
	print(i)
