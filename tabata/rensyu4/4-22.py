numbers = [0,1]

while  numbers[-1] < 100:
	numbers.append(numbers[-1]+numbers[-2])
	
for i in numbers:
	print(i)

