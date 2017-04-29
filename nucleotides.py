def nucleotides(DNA):
	A = 0
	G = 0
	C = 0
	T = 0
	for i in DNA:
		if i == 'A':
			A += 1
		elif i == 'G':
			G += 1
		elif i == 'T':
			T += 1
		elif i == 'C':
			C += 1
	return A,C,G,T

print (nucleotides('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'))
