import re
import os
def trans():
	path = r"C:\Users\user\Downloads"
	with open(os.path.join(path, "rosalind_tran.txt")) as f:
		data = f.read()
	Regex_Pattern = r'>Rosalind_\d\d\d\d'
	strings = str(re.sub(Regex_Pattern, ' ', data))
	newDNA = strings.replace("\n", "")
	newDNA2 = newDNA.split( )
	string1 = newDNA2[0]
	string2 = newDNA2[1]
	transversion = 0
	transition = 0
	for i,j in zip(string1, string2):
		if i == "G" and j != i:
			if j == "C" or j == "T":
				transversion += 1
			else:
				transition += 1
		elif i == "A" and j != i:
			if j == "T" or j == "C":
				transversion += 1
			else:
				transition += 1
		elif i == "C" and j != i:
			if j == "A" or j == "G":
				transversion += 1
			else:
				transition += 1
		elif i == "T" and j != i:
			if j == "G" or j == "A":
				transversion += 1
			else:
				transition += 1
	return (transition/transversion)
print(trans())