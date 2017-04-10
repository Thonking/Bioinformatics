def rabbit(n,k):
	total = 1
	if n == 1 or n == 2:
		return 1
	if n >= 3:
		total = rabbit(n-1,k) + (rabbit(n-2,k) * k)
	return total

print (rabbit(28,2))
