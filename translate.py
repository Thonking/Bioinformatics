def RNA2Protein(content):

    if len(content) < 1:
        return 'No input detected.'

    for i in content:
        if i is not 'G' and i is not 'C' and i is not 'A' and i is not 'U':
            return 'Only G, A, C, or U please.'
                

    if len(content) % 3 != 0:
        return 'Please give a sequence that has a number of bases that is divisible by 3'
        
    else:
        amino_acids = {'UUU' : 'F', 'UUC' : 'F', 'UUA' : 'L', 'UUG' : 'L', 'CUU' : 'L', 'CUC' : 'L', 'CUA' : 'L', 'CUG' : 'L', 'AUU' : 'I', 'AUC' : 'I', 'AUA' : 'I', 'AUG' : 'M', 'GUU' : 'V', 'GUC' : 'V', 'GUA' : 'V', 'GUG' : 'V', 'UCU' : 'S', 'UCC' : 'S', 'UCA' : 'S', 'UCG' : 'S', 'CCU' : 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P', 'ACU' : 'T', 'ACC' : 'T', 'ACA' : 'T', 'ACG' : 'T', 'GCU' : 'A', 'GCC' : 'A', 'GCA' : 'A', 'GCG' : 'A', 'UAU' : 'Y', 'UAC' : 'Y', 'UAA' : 'Stop', 'UAG' : 'Stop', 'CAU' : 'H', 'CAC' : 'H', 'CAA' : 'Q', 'CAG' : 'Q', 'AAU' : 'N', 'AAC' : 'N', 'AAA' : 'K', 'AAG' : 'K', 'GAU' : 'D', 'GAC' : 'D', 'GAA' : 'E', 'GAG' : 'E', 'UGU' : 'C', 'UGC' : 'C', 'UGA' : 'Stop', 'UGG' : 'W', 'CGU' : 'R', 'CGC' : 'R', 'CGA' : 'R', 'CGG' : 'R', 'AGU' : 'S', 'AGC' : 'S', 'AGA' : 'R', 'AGG' : 'R', 'GGU' : 'G', 'GGC' : 'G', 'GGA' : 'G', 'GGG' : 'G'}
        codons = [content[i:i+3] for i in range(0, len(content), 3)]
        protein = [amino_acids[x] for x in codons]
        strprotein = ''.join(protein)
        return strprotein
print (RNA2Protein('AUGAGUACUAGCAACCAUAACGUAAGCUAUCAGUCGCACAGUGUGGCUAAAGGGGUAGUGAUUUACGAAGAAAAGUUAUUGCAUGCUCAAACGUUGACUGGAAACCGACAUCGGACUAGCUUCAUGACCACGAAAUGGAAAAUACCAUUUUCGGAAGAAAGGGCUGCUCCUGGGACGUUCAUUUCCACCUUUCAACUAAACCUAACGUCAGCUUCUUUCCCAUUACUGAAAAAAGAGGCCCACCGCCUACUGCCAAUAAAUAGGCGGUCUGUGCGUUGCGUUGAGGCCAUAUCUGGCGGCGCAUGUGCCUUCGUAUCGAGAACUGUCUGCCUUAUAAUUCGCAUCAAACUGGUCCUAGCCGUCGUUUGGGAGUUACGUGCAAAGUAUUCCGAUCAGUUUCGAUUUAUCCUCUUUCAGAGAGUUCACCCUCUUUCAACAACUAAUAUAUUCAAGGGCGAUCACCUGGUUCAACACUUCUACUCAUUUAGAGGCUCUAGUAGCGUUCGGCACGCUACCCGCCAGACUAUGGUAGCUACCAAGACCAGGAAUGCCACGGAAUACUCCAAAGCUAACUUUGGCUCGGGCCAUUCCUCCCUCAGAUAUAUAUCACGCCGAGGUGAUAACCACACAAUUCUCGACAGAAGACCGACGUCCCGAACAGGCAGAGUACAUUCCGAAAGCAGAGUUAACCUGGACUCUAUGUUCACCAUGCUCUUCUCGUCCCCAAAUGUAUUCCCCAAGGAGCAUGUUAUUUUCUUAAAAGAAGUUAAUCGAAUAUUACGGAACGGUUCAUUGACGGUGGUGCUUGAGUUUGUCCACCUAGCAAGAGGAGCCUAUAUAUCAUCGGAAUCCCUACCGCGAGGCUUGUAUUCGGCCAUAUAUAUCCCUCGCCUUCCAGGUGAUCAGAUCCAGACCUACGGCUUUAUACACGGCCCGAACGCGCAUUUUUUUAAGGGUCUUGAAAUUUGGGUUACUUACUCCUUGUUAUGCAACUACGCAACGCUUGCGUCCAGAGAGCGUGACGGACCAAGUUUGCUCGCGCUCGAGUCUACAAAUGACAAGAUCCGGAGAUCGCGGUACCGUCGUGCCACAUACUCACAAAGAGUGAAACCAACACUCCGUGGGCCGUUGCUAAUUCCUGGAGCGGGAAAUCUAAUCCCGGCAUCGUGUACAUCGCAUACAGCCAACUUGCUCCGUGUGCCCAGCCCGGUCGUUAACCGGCCUUGGCCCAGGUGCUUACGUUGGGCAAUAUCUAUAAGGCUGAUAUUAUUACUAUUAGAAGAGCAUGCAAAUACUGACGGAACUGUAGUAGCGUCUUUGCUUUCCCCGUUUCACAUGUGUCUUAGGGCAACCCGCUUGGGCGCCGGAAUCACAUGCACUCCCUUAGGUCUCUGGAGUUGUAGGUCGUUCGUGAUCGUGAUCAUCCUCUUCGCGUACUUAAGUUGGGCGUUAGUUCGAUCCUCACGGAUAAGACAACUCUACGCCAGCAAAGCAGCGUGGCACUACGCACUGGUAAUUACAAGUGUCGAAGCAUUUUGCAAUCACUUGCGAAUUCCGGAAGAGCGUCAGUAUUACCCUACAGUUCCGAAAGAAAUAUCUCUAACCCUAGAGGAUACAGGGGUUCCUUUACUCGCUUCGCCGCUAUACCCGAACUUGUCGAACACGCUGUUACCUGGGGUUUCUAUGCGGUACUCACAGCGCCCAGGUGCACGUAGAGUUUAUGGUAACCUCAUAUAUCAAUACACUCUUGCACGACCGCUGUUUUCGUAUCCUAAAGUUGGGAGUUACCGCAGAGUCCCCUGUCUGUGUUGGAUUAUUACAUGGCGCUGGACUGAGGUAGUUAAGAGUGCACCUAUUUAUCUGUGUUCUACGAAUCAGUCGGCUAGAAGGGAUAUACUGAGCGGUGCACCGGUGGCACCAUACCCUGAUCAUUCUGAGGCGUGCCUCAGCCAUGAAACCAGAACCAGUUCUCUAACCUUGCGGCGUGGGCAGCCUUUGAUGUCAAUGCGUGCAUCUAGCAGAACGUAUGCUACCAUGCCAUUCCCGCAGCCCGAGUGCGUUGUGCUUGGCCUUUAUACUCACUCCUACGGUGCCUUUCUUAUUGGCUCUGGCUCGGAAUUAUGUAUGUGUGCGUCGGGUUUCUGCCGACGUAUACCCUUACCGCUCUUUCAGCUUCUUAAUGCUAAAGGAAGGCUAGUGUCUAAUCUGAAGAAACCGUUCUGUGAAAAAAAGACGAUUUGGUUAUCGUUAUUGAAUCAGGUUCACGUACGUUACGCGACCUCACGUUCAUCCGCAGACAGUGGUGACCAUUGUAUUUUCUCAGCGUUUACAGGAGAUACUUCGGAGGUGACCUCUAUUCAGGCUUCCAUUGGCUAUGGUUAUCCGUGGCACGUUUAUCUGGGGCCACGCCCUAGAAUCAGGGACUCACCCCAUCAUAGACAUCGGGCCUCGCGGAUCGCACGACCAAUAGUCAGCCAGUCAGAAGUGGACGGACCCUCUACCGUAAAAGUGAAGUUUACCCGCUUAGCAUUUACACCAACCUCAUGCGUCAAGAUCGGGACCCGCUGUUCUGUCAUUGCGGCUUCAAAAGCACGUAGCUACCGAGUACUGCAUUCGGGACUGAUAGCUUACAAUUCUGAGGUUAACAGGCGUGGAAGAACUGAUCGUAAUGGUAGAACGGAUGGUUUGCGGUGCAUUUCUCCAUGGAAUUCCCGAUUUCUCUCGAAUCGCUUUGUUAUAGGACUGUGCCUAGAGAUGGUCUUAGCGCGCCCUGGAGGAAAGAGAGAGCUCCUGUUUUCCGGCAGUAAGCGACAUAGUUUUUCUUCUCCGAGUACCUACAUGUUGAGCGCACUAUCAGCUGUUCGAAACGGCGCUGGUACAGCUGUAGCGCUAGCGUUGAAGACGAAAAGUGCAUCUAAACAGUCAGACACCAGCCGGAAGGCCCAUUGUACAAUAGCCAUGGUACAUGGGAAUCGUCAGAUUCGGUCGCCUGCCCGUGAGGGUUCCGCUGCCAUGCUGCUUGGCUCUUCCUGUUCCAAAGGGCAUCGACAGGUUAACUCUCGCCGUGGAUCCGCGUACCUUAAAAGCACCGAAUGGGAAACUCGGGGUUAUUGGAUUUCCAGGCGGCAGGCACGUCUUACAUUCCGCUCAGCGAGCGGCUACGGUUUCCCUAGUCCUGAAUUAUGUAACGUAGCCCGGGCCCCUACAGGACCACCCUCGCUUAGUAAUAGAAGCGCUAGAUGCUUUAGACUACGACUUAUAUCGCCAGGCCCAGACAACGAAUCCAUUGCCAAAGCCAGAUCGAAUUCCUCGAUUUCGCUUAAAAGGAGUAUGGCGGGUAGCGCCCAAAGUGAGUGGAGUGGUAGCUGGGCGUGGGGAGUAGACGCUUCGAUGAUUAGUCAUCCGAGGCACAUUACUAAGGUUAAUUUCCGCUGGGGUCGUUCCCCCUGUAACUAUCUGCGGUCAAUGUGGGGAAUCCUGCUAUACAAUGAGACAACCCGCUGGUGUCGUGCUCGGGAGGAUUUACCUGAUUGUGUAAACGUAGAGUCAAACUAUCGCUUGUUCCACUUCUCCGCGGACGGUAUAGGAUCUCAUAGGUUCCGUGCUGCUACCGUUAGGACUGCUAUCGGUAAUCCCCGCACCAAAGUUGCAACGAUCAACAGCUCUGUACACGGCAACUUGUCGCUAUUAACUGUCUCCUACCACUAUCGGAAUAGGUCUGGCUCGUCGGAUAGGCCGGACUUAGAAUCUCCUUCGGCCUUGAGUAGAAUGAGGAAGUUUUCCGUCAAGGUGCCGUCGGUCAAAGGCUUGAUCGAAAUACAUUGUUCGGAAUGCCCAUGGGCAUACAUUCAUUUGCAGGUAGCACUGCCGCUGCCAGCAUGUCCCGGCCCCGUCGGGGCAGGAACUUCCCUAGCGGGAAAAGUGUCUUCACUCAUCCCGGGGGUGAUCCGAACUGUCAACGUCCUAAACAGUAUAUUGCACCCCAAUUUCACGGUCUCCACUGCUGGAGCAAAGCAAUCUGUCUGUGCACUGAGUGCGCUAGGGUUCCUAUCCCUAUGGCCUAACUACAUAUCCACCGUAAGUCAACACAGGCUCCGACUACACGUCACUCGGCACUUAGUUGAAUCCGCGUUUCCAACUAUCAAAAGCGUGUGGCUUAGCCUUUCCCGCGCAACAGCUCUACGACUACUAGAUGCGACGACUGUGAGGCCUCGAGCUCGACCCAUAAGAUGUACCUCCCAGUUAUCAAAAAGCCUAAAGGUAAGAGCGGGAUAUAGAGUCAGAUGGAAGCGCUCAGGCGAUGCAAGUAGCGGAUCCGGAUCCCUGUUACAACCGUUGGCGCUAGCGUCAAGACAAUCGCACUUGCAUGGGGGCUCGCGUCCGGGCCGGUUGGAUGAGACAAUAUAUCGGACCCCCGUGGGCACAACCUACCUGAUAAUUCAGAAGGGACAGCCCAAGCCACGUCCGGUCAAGGCUGUUAGUAGCGUCCGUAGGACCGCCUUGGCGUAUUCCGUACAGAAGGCGACGCGGUGUGUGGGGUUUAUAGCUUCCGCUAACUCAACAAAACCGAACAAUAUGGGUCCGACUAACCUGAGUCCCCUAAGCCUACGCGUCAUACUGUUCCCCGCCAAUUUCACAGAAAUCUUACUAGUACACCAGAAGAGUAGUUCGGCUCAGCUUACGAGCUCACUCACUAUCUCACUAAAAAAUUCGAGCCCCCAAAAGUUUCGAUCACGCGGUGACAUCUACUGUGAUUACGUGCGGGGGAGACAUGCUGAAGUCAUGUUCCUUUUCACGCCCGUCUAUCAGGGCGGGGGAAGGAGUUGGUAUUUUGUGUCCUACAUCGGGGAUUGGUUAAGACUCAUGCUGAUGAUCACUGAAUUCUCAAACACAAUGCAUGCGUCUGGGUUAACACGGCUCUGGGAACAUGCGUUCCUUCGACGUCUGGAUCUCCCUACGAGAUCGUGGGGCCCUUUUGGGCAUGAGUCAUUUGAAGACUGUCCAGAUCUUCGCCAGCCCAUUUGUAGUUGCGUUCAUUUUUUGCUGUUCCCUAUGCACGCCGUACUCAUCGCGCGGUCCCGUGCGCGGGGGGCUCGCUUCUGGGAGGCAAUAACAGAUAAGAGGACCUGCAGAGCCCAAGGAUAUAACCUUAGUUCCUAUCCUUCUGCGUUGACAGCUCGUGUUACUAACGCCCUGCGAGCGCUUCUCAUAUGUUCGCCCCAAGUGCGGAGGGCACCGAAGCGCACUUGGCAAUUAACACUGAGGAGCACGAUAACACGUAGAUUCAGGCGACCUCCGGGGAUUGUCACCCGGCGACCACUAUGCCAUCAGGGCCUGCUGGCUACGGAAGGGUCAAAAACGCGUCGUGUGUCUCGCAUGAGGUCUACCGGUAGUGGUCCUGAUGCAUUGUCACCCCGAAUUGCGAAACUACGACCUAGAAUAGUGUGCAUAACCUGGGAUGUUCAAUCUUCCCGGGUCUUGACCGGCAGCGAGUUGGUAUUCAGUAUGACUAUCCUACCCGCCCGGAGUCCAGUAUUCAUGCUGCCAACGACUUAUUAUCAAUACUCUAAGACAAUGUCGGAGGGGAUUGUUAAGAACCCCUCAUCAAUUGUAAAAACGGUGGGCUCCUGCAGAGUCCCACAAGCUAUGAAAAAGAGCUUAAAGUCGGUUUCAUCUAUGACCCCCCCACAGAUAUGCCAUUCUCAACUGAGACCUCGUCUUCAGCUGCACAAACCGAGUACCACCGACGCGGUCCUCGCGCUAACGCCGCAGGGAGCAAUUAAGCUUUUGAUCUACACUGAGUGCGGGUCGGGCCAACGAAGAGACGGCCCACGCAGGACGGUACCUUGGCCUCAGACCGUCGUCAAAGAAGAUAGUGGCGGCGCGUCUUGGGCGGGGGCGAGUCCGGACCUGUCACAGGACCACGUCCUUAGUACAACCGAGGGAUCUGGCCAAAAGUUCGAGAAGACUUCCAGCAGCCGUUCCCCACUUACUAUCAUUCAACUAUUAGUGAUAAGAUCCGUAGCUUGGGCAACACUACUGGAUGUAGGACUGCGGACACACCAGUGGCUGACCUCUCGCUGGCGGGCUGUAAGACUGCAAAUAUCCGUCGUGAAGAAUAUGGCUUGGCCUCAGGAGAGUAGGGUGGUGACUCUUAACAGGCGAUAUAGGGCAGUUGGCCAAGCGAUUAGUUCGUAUUACCAGAGAUGCUUAUUAGUUAGACUCGCGGUGCGUGCUAGCCAGCAACCGGGCCCUCCAUCACAAUAUACCAGGCGGCAAGCGAAUAUACAGGGCCCUGCGCAGCGUCCUAUGGUCUCUUGUCGAAAACAUGGUGCUGCCGUGCACGGGCGUACCCCGGUUUUGCACAGUACCUUGAUUCUUGUAGGGAAAAAGCACACUUCCCUAUCUCAAGGAGCAGACUUGAUAUUGCAUGGUGAAAGUAUAGAGGUGCAUGGUCAUAUCAUAUUGACGUUUUCACGUUCCCAGCGACGAGCGCCGUCGGACACCCGUAAGAUUGACCAUCGGCGUGUUCGUUAUACUACGUAUGCCAAAAGGGUCACCCGGAUCAGGGCCGCCCACGCUGGACGGUUUCCUUUGUUGCGAAUAAUGAAGAAUCGCACUAAACAGAUCGCGUUAGAGACUGGAUGUACUAUACUACCUUAUCGCAAAAGUGUUGCGUUAAUAGCGACCGCCUGUAAGGGUGUAGCUAGACCUGUUGAAUUCGCGACGACUCAAACUCCUUCCGCUGUAGGCGAGGUCGGUUACAUUUACAAGGCCCAUAUAUAUAGUGUCCGCCCAAGGGACAUCUGGAAAGUAGGUACUGCAUAUGAUGAGUCAGAGUGGCACAAUCGUGAGUUGCCUUUAAUUAACCUUUUACGACGAAACCGUUCCUUUGUGAACCACACAAUGGGUCGGACCCUAUUUAGAACCAUCCGACCGGGACGCCUCGAUAUGGCUAAGACUCUCCUGCGAGCCGGCUCAAGAUCGUACAAGCUAACUUUAACUCAACCAAACACCAACGCGCCGGGGUUUCUGCCAAUUUGUUGCGGGGCCCCAUUCCACGUACUUAUGAUAAAUUGUUUAAUUAUCCCGGAUCACAAAAGCCGAGAUAGAGUAUGCAGUAAACUGUGGCUGGGAGGAAGCCCUGUGAACUGGUCAGCAGGGGUGCCUGCGCCCGCACAGUUCCACGUCGGACACCAGCUCGAUACACACGCGUACGCCUCUAUUCCCUUCUACGAAGGCAUCAGUUCUGUCUCGCCAAAGGCUGGCGGGCCGUGGCAAUCUCAUCAACGCGAAGGCUGGGUAGUGAAGUGCCCGCAUGGGUUAAGAUGGUCCAGAGAAUCAUCCCAUCCCGGAUUUCGCGCAGACUGUGAUGGAAAUCUGUCGCAACCGUUUCAUCAGGAUUUCACAGACAUGCUGUACAGACGCGUAUACGGUUACCGUGUGGGAAGUCAACGCUGGAGAGCGGCAUCGCGUUUGUUAGAAGGAACCACUACCAUUCAUCCUAUGACAGACCCUUAUGAAGUGGUAGCCACUCUACAAGUGAUUCACGCCAUAGAAGCUGGACAAGUGGCCCAUGAACGACCCUACGUUUCUCAAUCAUUUAUGAUCUCAUGCCGCCUGAUCGCGGGCCGUGGAAGAUCACCGAUCGGUCAUUCCGACAUUAAAUCAAUAAUCGUAUUGCACAAAAGGUCCCCAUCGUGCAAAGUGGAUUUUUCAGCGCCUCCAGGGGUCGAGGACGUGGGUUGCGUGCAGAUAUUACCUCAAUCUUUGCUACUCGUUCAGACAUUAAGUGCUUGUUCACCUAAGUCACCGAAGAGGGGCUUAGCCUGUGAGGGUAUACGUCAGUUCACCGCGACGGAAAACCUCACGGCAAGCAGGGCGACUUUUUACAAAAUUCUUCUAACUGCAAACGUAGUGGAAAGACACUCCCGCACACUUCCGCAGGAAAUGAUGGCCAUCGCACAGCGUUCAAACCCGAUCUUAAAAUGGAGGCUUUCCCACGUCUAUGUGGCGAUGUUCGGCGCCGCGAGGUUGGAUUUCCAAAUGUGCAUGACGUCGCACUGUCCUGGUAUCGUUUUUGAGUGGCCCCGAUUGGUUGCUUGGGGUUUUGAGUAUAACAUAUUCCCGCCUGCUCCUGGCCUCGAAGAGGCGAGACCUUCCCGUGCGGCUUCCACCAGCCAAGGAGGGCUCAAAGCUGGCUUUUGCGAGCGGCUAGCGUGGUUUCGGUGGCUACAAGCGGCUGUUUUAGAGAGCAGUAGUUCCACAAGGUGUUUCCCGCAACUGUGGGCUUGGAAAAUUAAUCUCCCCGAUACACGAAUCUCAAGCACUCGCGGGUGUCUACGGUUCCGUGCGGAGGCUCAAAAACAGUUCACCAGUAGAAUGAUUGACCGUGAAACUCACGCUUACGCAUGUUGGAUACGCCAUUGCGAACAUCUGUGCGGACGUGGCGCCUGUUCGGCACUCCCAGUCCAAUAUCGAAGGACGCCACUAUGCAGUCUAUGUGUUGAGACCGCUAUUCGUUAUGUAGCGACGUUUCGUGAAGGACGAAUCGCACUUACCGUUAAAGAAAAUCCGCAGUUGGGGACUGAAGCGAAAUCCUUUUUCUCGGGAAGUGUAGCGCUCAAAUUCGCCCCGCGCUCUACCGCAACUCGGUACGCGACUUACAAUGUAUAUGUCGACGUCCAUUACGCUGCUAUUGGCACGCCCCGCACAAUCUUGGCCAUCUCACCGGAAAGCAUCUCAACAACUACCCAUAAUGCACCCCGUGGAGAAAGCGUCCCCAUGGCAGGGAAUCCGAACCAAUACCACCCAACUUUCUCAUUCCAGAAACGUCUUCGCUGCCUAGGGACCACGUUACUCACGGGGAUAAUUACACGUUCAACCACAUUCGCAAAAUCUCUGAAACUUAGCAGGAUGAUUACGACGACGCGGUACUUCGACGGAUGUACCGGUGUAGGCUUUGGGUUCAAUGAGAACCGUCCGAUAGUUCCGGUUCAACACUUAUUCAGCGUGCUGGUAGGUACCUCAAUACUACCAGACCGUUCGAAAAUGUCGGAUUGCCCCCCGUUCAAUACAGCAUUCAAGACUGACUCCGGUCCCGCUUCCGCUAAUAUAGUUGGUAUGGCCGGGUACAUGGGGACCCUCCGUUACACGUGUACCAUUGUUACCAAGACAUCCAUUACAGAUGUUUUGCCGAAGAGACUGCAUGCGGACUAUACUAAUAAUCGUAUCUCCAAAGACGGCUUGGAGCAGGCGCUUUCCUCAGAAAACCACGAUGGCUCACUGCAACUUCUAAGAACAAACUCAGGCACUUGUCAACACCUCGAGUUGCAGGUUCGCUCCGACCGUGUGGUCGUUGAAUGCGUAGAUUUCGCCCUCCCUAAUAACACCACGCUAUCUAGAUCAACUAUAAAUACAAGGACUAUGUUUGUCUCCCAGCACACGACUCGAUACUCGCCAGAUAUCCCAUGA'))