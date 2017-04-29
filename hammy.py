def hammy():
	a = input('Please input the first string: ')
	b = input('Please input the second string: ')
	hamming = 0
	for i,j in zip(a,b):
		if i != j:
			hamming += 1
	return hamming

print(hammy())



