def reversecomp(DNA):
	reverse = DNA[::-1]
	comp = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}
	revcomp = ''
	for i in reverse:
		revcomp += comp[i]
	return revcomp
print(reversecomp('GAGCATATCAAATACAATGTCTCCTACCCAAGGTTCTCTCGGACCGCTCGCTTCTGGACGGACGATCTTACCTGGTGTTCGTACGTAAAGTAACCAATAATCTCTTCTCTCTAGTTGAGGCCGATTGTGGCGTCGGAGCAAGCGCATTCACCAGCCTGCACCCCCACTATAGGTCCAGGAAGGGAAAATCAAGGCAACGAAGTACCAGCCCGACGAATACCTCCCGTTCGGCGCTCGTCGGGCTGGTTTCCGGGGCGAATTCAACTCATTGGTCAAGACTAGAGAACTACCTGCACTAAGCGTGGTGCGAGGACCGTTGATGAAACGGAATTGCCAGAAGAGAATGTCCACGGTCATTAGGGGTCCGCACGGCGCATGGCCTGTAGGTTGCGACGGCTCACCCAAACTAGAAACTTGCATCACAGTATATGATCATAACAGAAAACGAGGCCAGCCGATTTGCTCGGATAAAAGCTTCCGTTCCTCGTGGCCACTTGTAGTATTGAGCAGATAGTATGCGCTCGGGGTCGCCGGCGAGCAAAGAAGTTCGAAGTGGTCGGTATACCTCTGTTATTTTGGCAATTGTACCAGACGTTGGAGCCACTAGTATGCCCATACATTGTCCAAGGTTGTATTGCGTCATTAAAGCCCTCGTCCTGTTGTATAATACCACCACGGAAGGCCTCATGAAATTGCAATAAGCTAGACGCGTACTCTGTCCAAAACGATGCTTCCTTTTATGACATTAACTTTCAAAGTCCGGTGTGGTTAGTTATCCTGCAGACTCAAACTTGCAAAATGCGATCCTAGTACGATATGAAGAAATTTGAATTTCGATTTACGACCTGCGAATTAATAGCATACAGTGACATAC'
))
