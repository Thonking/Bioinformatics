import itertools
import re
import os
def lexf():
	path = r"C:\Users\user\Downloads"
	with open(os.path.join(path, "test.txt")) as f: 
		data = f.read()
	RegexPattern = r"\d+"
	alphabet = r"[A-Z]+"
	alphalist = []
	for i in re.findall(alphabet, data):
		alphalist.append(i)
	n = int(''.join(re.findall(RegexPattern, data)))
	string = ''.join(alphalist)
	for i in itertools.product(string, repeat=n):
		print(''.join([str(j) for j in i]))
lexf()
