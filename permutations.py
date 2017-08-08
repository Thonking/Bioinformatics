import itertools

def permutations():
	number = int(input("Input number here: "))
	permutation = list(range(1,number+1))
	memes = []
	for i in itertools.permutations(permutation, number):
		memes.append(i)
	total = len(memes)
	print(total)
	for i in memes:
		print(*i)

permutations()



