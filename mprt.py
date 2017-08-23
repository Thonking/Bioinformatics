import urllib.request
import re
import os

def N_glycosylation():
	path = r"C:\Users\user\Downloads"
	with open(os.path.join(path, "proteinids.txt")) as f: #parse IDs from file
		data = f.read()
	newIDs = data.replace("\n", " ")
	newIDs2 = newIDs.split( )
	proteins = []
	positions = []
	proteinsIDs = {}
	for i in newIDs2:
		memes = 'http://www.uniprot.org/uniprot/'+i+'.fasta' #get protein data from sites
		with urllib.request.urlopen(memes) as f:
			data = f.read()
		data2 = data.decode("utf-8")
		
		Regex_Pattern = r"^>.+\n"
		string = str(re.sub(Regex_Pattern, '', data2)) #parse out protein sequences
		newProtein = string.replace("\n", "")
		proteins.append(newProtein)
		proteinsIDs[newProtein] = i #organize proteins and respective IDs into dictionary

	for i in proteins:
		Nglycosylation = r"(?=N[^P](S|T)[^P])" #find matches in protein sequences
		match = re.search(Nglycosylation, i)
		if match:
			print(proteinsIDs[i])
			for j in re.finditer(Nglycosylation, i):
				positions.append(str(j.start()+1))
			print(' '.join(positions))
			positions = []
N_glycosylation()






