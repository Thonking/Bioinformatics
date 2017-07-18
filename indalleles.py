from functools import reduce
import operator as op

k = int(input("generation: "))
n = int(input("number of AaBb: "))

N = 2**k
K = n

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, range(n, n-r, -1))
    denom = reduce(op.mul, range(1, r+1))
    return numer//denom 

def indalleles():
	answer = 0
	combsanswer = 0
	for i in range(K, N+1):
		combs = ncr(N, i)
		success = 0.25**i
		fail = 0.75**(N-i)
		answer += (combs * success * fail)
		combsanswer += combs
	print(combsanswer)
	return answer

print(indalleles())

