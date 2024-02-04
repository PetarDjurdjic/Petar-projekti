def MotifEnumeration(Dna, k, d):
    Patterns = set()
    for i in range(len(Dna) - k +1):
 #get all patterns that can be found in first string
 #at most d will be the neighborhood of that pattern
        pattern = Dna[0][i:i+k]
        neighborhood = Neighbors(pattern, d)
        for neighbor in neighborhood:
            if isPatternInAll(neighbor, Dna, d):
                Patterns.add(neighbor)

    return list(Patterns)



def Neighbors(pattern, d):
    neighborhood = set()
    nucleotides = ["A", "C", "G", "T"]
#case 1: only 1 letter
    if len(pattern) == 1:
        return nucleotides
#case 2: we have a hamming distance of 0, so no neighborhood possible
    if d == 0:
        return set()
    suffixNeighbors = Neighbors(pattern[1:], d)
    for i in suffixNeighbors:
        if HammingDistance(pattern[1:], i) < d:
            for nucleotide in nucleotides:
                neighborhood.add(nucleotide + i)
        else:
            neighborhood.add(pattern[0] + i )
    return list(neighborhood)
            


def HammingDistance(genome,pattern):
    mm = 0
    for i in range(len(genome)):
        if genome[i] != pattern[i]:
            mm +=1
    return mm


def isPatternInAll(pattern, Dna, d):
    for string in Dna:
        found = False
        for i in range(len(string) - len(pattern) +1):
            substring = string[i:i+len(pattern)]
            if HammingDistance(pattern, substring) <= d:
                found = True
                break
        if not found:
                return False
    return True



d = 1
k = 3
Dna = ["AAATTGACGCAT","GACGACCACGTT","CGTCAGCGCCTG","GCTGAGCACCGG", "AGTTCGGGACAG"]
print(MotifEnumeration(Dna, k, d))