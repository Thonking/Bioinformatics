def mendel(k,m,n):
	p = k + m + n
	prob = ((k/p)*((k-1)/(p-1))) + (((k/p)*(m/(p-1))) * 2) + (((k/p)*(n/(p-1))) * 2) + (((m/p)*(n/(p-1))) * 0.5 * 2) + (((m/p)*((m-1)/(p-1))) * 0.75)
	return prob
print (mendel(25,29,21))