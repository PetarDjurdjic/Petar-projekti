def MedianString(Dna, k):
    distance = float('inf')
    Patterns = AllStrings(k)
    Median = []
    for i in range(len(Patterns)):
        Pattern = Patterns[i]
        if distance > DistanceBetweenPatternAndStrings(Pattern, Dna):
            distance = DistanceBetweenPatternAndStrings(Pattern, Dna)
            Median=Pattern
    return Median



def AllStrings(k):
    bases = ['A', 'C', 'G', 'T']
    array = bases
    for n in range(k-1):
        array = [i+j for i in array for j in bases]
    return array

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern)
    l = len(Dna)
    distance = 0
    for i in range(l):
        hamming_distance_min = float('inf')
        for j in range(len(Dna[i])-k+1):
            if hamming_distance_min > HammingDistance(Pattern,Dna[i][j:j+k]):
                hamming_distance_min = HammingDistance(Pattern,Dna[i][j:j+k])
        distance = distance + hamming_distance_min
    return distance




def HammingDistance(genome,pattern):
    mm = 0
    for i in range(len(genome)):
        if genome[i] != pattern[i]:
            mm +=1
    return mm





# Dna = ["GGAAGTGGAGGCGTTTCACCAAAATAACCAATATGTCAGCCT",
# "CTACAGCTGATGCAGCTTCGCACCACTTGCCGGGGATCACGA",
# "CCCGGTTTTTTTACCAGTTGTGTCCTTGCGCAGCGTCAGTAT",
# "TTTAACTCCAATCTTGGACAGCATAAAATCTCGGATGACAAG",
# "TCCCCCTACCGCATATCCTTACGTTTACAGCAGCCTTCCACC",
# "CAGCGTTTGCTTTAAAGATTCACCTATGTATAAGGCATCCCG",
# "TGTCTCTCCAAGGGCTCGCAGCATGGTTGAGAAAACTCCAAT",
# "CAGCGTGGTTAATTTGAGAGCGGTGTGTACGATCTTTCTGAT",
# "GGAAAGAGGTCCCTCGCACCATCGTGTGACCAGCATTTTGTT",
# "CAGCATAGGGTGTAGGGGCAGCGTCAACAGGTGTCGTGCGCT"]

Dna = ["CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC","GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC","GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG"]
k = 7
print(MedianString(Dna, k))
