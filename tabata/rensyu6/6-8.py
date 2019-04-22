class Exercise:
	def __init__(self,n):
		self.n = n
	def fibonacci(self,n):
		numbers = [0,1]
		for i in range(2,n+1):
			numbers.append(numbers[-1]+numbers[-2])
			result = numbers[-2]+numbers[-1]
		return result

exercise = Exercise(20) 
for j in range(10,20):
	print(exercise.fibonacci(j))

