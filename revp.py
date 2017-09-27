import re
import os
def revp():
	path = r"C:\Users\user\Downloads"
	with open(os.path.join(path, "rosalind_revp.txt")) as f:
	    data = f.read()
	Regex_Pattern = r'>Rosalind_\d+'
	strings = str(re.sub(Regex_Pattern, '', data))
	newDNA = strings.replace("\n","")
	comp = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}
	compl = ''
	for i in newDNA:
		compl += comp[i]
	for f in range(len(newDNA)):
		for j in range(f, len(compl)):
			site = newDNA[f:j+1]
			revsite = compl[f:j+1]
			if len(site) >= 4 and len(site) <= 12:
				if site == revsite[::-1]:
					print(f + 1, len(site))
	print(newDNA)
	print(compl)
	
revp()
