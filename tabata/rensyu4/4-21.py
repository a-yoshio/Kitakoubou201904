size = int(input())
for i in range(size):
	for j in range(size):
		if j == i or j == size-1-i:
			print("X",end='')
		else:
			print(" ",end='')
	print(" ")

