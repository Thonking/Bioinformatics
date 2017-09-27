def parper():
	number = int(input("put k here: "))
	number2 = int(input("put n here: "))
	memes = 1
	for i in range(number2-number+1, number2+1):
		memes *= i
	return memes % 1000000
print(parper())