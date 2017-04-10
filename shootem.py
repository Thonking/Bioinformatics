def fizzbuzz():
	for i in range (0, 101):
		if i % 3 == 0 and i % 5 == 0:
			print('FizzBuzz')
		elif i % 5 == 0:
			print('Buzz')
		elif i % 3 == 0:
			print('Fizz')
		else:
			print(i)
print(fizzbuzz())