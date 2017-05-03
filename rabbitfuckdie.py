def rabbit(n,m):
	meme = list()
	for i in range(n):
		if i < 2:
			total = 1
			meme.append(total)
		elif i < m or m == 0:
			total = meme[i-1] + meme[i-2]
			meme.append(total)
		elif i == m:
			total = meme[i-1] + meme[i-2] - 1
			meme.append(total)
		elif i > m:
			total = meme[i-1] + meme[i-2] - meme[i-(m+1)]
			meme.append(total)
	return total

print (rabbit(87,20))
