import re
import os
def consensusprof():
	path = r"C:\Users\Nathan Chan\Downloads"
	with open(os.path.join(path, "rosalind_cons (1).txt")) as f:
		data = f.read()
	Regex_Pattern = r'>Rosalind_\d\d\d\d'
	strings = str(re.sub(Regex_Pattern, ' ', data))
	newDNA = strings.replace("\n","")
	newDNA2 = newDNA.split( )
	lol = newDNA2[0]
	profile = {"A":[0]*len(lol),"C":[0]*len(lol),"T":[0]*len(lol),"G":[0]*len(lol)}
	for j in newDNA2:
		#please kill me
		for k,i in zip(j,range(len(lol))):
			if k == "A":
				profile["A"][i] += 1
			elif k == "G":
				profile["G"][i] += 1
			elif k == "T":
				profile["T"][i] += 1
			elif k == "C":
				profile["C"][i] += 1
	consensus = ""
	for i in range(len(lol)):
		if profile["A"][i] >= profile["G"][i] and profile["A"][i] >= profile["T"][i] and profile["A"][i] >= profile["C"][i]:
			consensus += "A"
		elif profile["G"][i] >= profile["A"][i] and profile["G"][i] >= profile["T"][i] and profile["G"][i] >= profile["C"][i]:
			consensus += "G"
		elif profile["T"][i] >= profile["A"][i] and profile["T"][i] >= profile["G"][i] and profile["T"][i] >= profile["C"][i]:
			consensus += "T"
		elif profile["C"][i] >= profile["A"][i] and profile["C"][i] >= profile["G"][i] and profile["C"][i] >= profile["T"][i]:
			consensus += "C"
	print(consensus)
	print("A: " + " ".join(str(x) for x in profile["A"]))
	print("C: " + " ".join(str(x) for x in profile["C"]))
	print("G: " + " ".join(str(x) for x in profile["G"]))
	print("T: " + " ".join(str(x) for x in profile["T"]))
consensusprof()




