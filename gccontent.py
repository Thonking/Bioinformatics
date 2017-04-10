	
def calculateGC(DNA):
	gc = 0
	newDNA = DNA.replace("\n","")
	for i in newDNA:
		if i == 'G' or i == 'C':
			gc += 1
		percent = (gc/len(newDNA)) * 100
	return percent

def GC(yes):
	maxgc = 0
	track = ''
	for key in yes.keys():
		if calculateGC(yes[key]) > maxgc:
			maxgc = calculateGC(yes[key])
			track = key
	return track, maxgc

yes = {} #add id:DNA string dictionary here
print (GC(yes))




