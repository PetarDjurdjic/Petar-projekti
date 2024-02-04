import random

def RandomMotifs(Dna, k, t):
    motifs = []
    for i in range(t):
        rand_num = random.randint(0, len(Dna[i]) - k)
        motifs.append(Dna[i][rand_num: rand_num + k])
    return motifs


Dna = ["TTACCTTAAC",
"GATGTCTGTC",
"ACGGCGTTAG",
"CCCTAACGAG",
"CGTCAGAGGT"]

k = 3
t = len(Dna)

print(RandomMotifs(Dna, k, t))