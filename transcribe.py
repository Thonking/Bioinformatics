def transcribe(DNA):
	new = ''
	for i in DNA:
		if i == 'T':
			i = 'U'
			new += i
		else:
			new += i
	return new
DNA = '' #insert DNA sequence here
print (transcribe('AAATCCTACTGACTAGTCAGACCACGCGATTTCGTAACGACCTCCTTCTCCGGATAGCGTTGCCCAGAGCAACTCTTGGCCCAAGCTGGCTCCTAGAAACTACTTTACACGTCGGGTATGTCACCTGAGACATACGTGCATTCAGTCCCATAAACACTCTCGAGCATATGCCGAGGCCTTTGTGATTCCCACCACCCTGAACTGTGATAAACTCACGCCCTCGAAGTTATCGCTCATGATAACAGGGGAACGAAAGAGTCTCGTAAACGAGATCGCACTAGTTAGCATTGTTCGTATTGGGCTCTTTCCGTTCATTGTGCCAGCCAAACTAACATGCGTGTATTAGTCCCCGGCCCCATCGCCTACCTGGGTGACCACGGTAGGCGAATCTTTGCGACGCATTACCGGATTAGTGTCGTCCCCGCCACTGACTTACTGATCAACCTGACATTACATTTTCAGCCCTGACAAACGGGACACGGACTTATAGCCTAGGGTTACCTGTGCTGTAAATCATCTTTATCAGTGAGATCCAAACGAACCGTGACCAGCCGCACGCACCGTGGGATAGCTGCTTGTTGAACAAATTCCGAATGGACAAAGCTTCAGCGTTCATACGCCAGGTCCTGAAAAGCCAGACCGGTGACGGAACGTTAGTCTTACTTTGCTTGTATTTGCATAAGACTACCTCCTTGAAGTCAGGGCGCTTGAGGTCCACTCCCCACGAACTCTTGTGGGCGTGCGCCCCGCCTCTATATACAATGTCACTAGACGAATCCCTCGAGGCTCATTACCCCGCAACTCCAACAGACTACGGTATCGACTGCCATCTGTGGAAATCGCGATTTGCGTTCTGATAGTCACCTGTTAGTTTAACACAAGGCCATCTGCGACGTCATGGGTGGGATCATTGGGGCTACGCTGCTTTGAGGCTACA'))