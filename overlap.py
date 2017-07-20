import itertools
import os
import re
def overlap():
    path = r"C:\Users\user\Downloads"
    with open(os.path.join(path, "rosalind_grph_3_dataset.txt")) as f:
        data = f.read()
    Regex_Pattern = r'>Rosalind_\d\d\d\d'
    strings = str(re.sub(Regex_Pattern, ' ', data))
    newDNA = strings.replace("\n","")
    newDNA2 = newDNA.split( )
    path2 = r"C:\Users\user\Downloads"
    with open(os.path.join(path2, "rosalind_grph_3_dataset.txt")) as f:
        data2 = f.read()
    RegexPattern2 = r'\n[A-Z]+'
    IDs = str(re.sub(RegexPattern2, ' ', data2))
    IDs2 = IDs.replace("\n","")
    IDs3 = IDs.split( )
    meme = {}
    for i, j in zip(newDNA2, IDs3):
        meme[i] = j
    for i, j in itertools.permutations(newDNA2,2):
        if j[:3] == i[-3:]:
            print(meme[i] + " " + meme[j])
    
print(overlap())