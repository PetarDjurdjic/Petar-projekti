def readGenome(filename):
    genome = ""
    with open(filename, "r") as f:
        for line in f:
            if not line[0] == ">":
                genome += line.rstrip()
    return genome

genome = readGenome("chr1.GRCh38.excerpt.fasta")

def naive_with_counts(p,t):
    occurrences = []
    num_char_comp = 0
    num_alignmets_tried = 0
    for i in range(len(t) - len(p)+1):
        match = True
        num_alignmets_tried +=1
        for j in range(len(p)):
            num_char_comp +=1
            if t[i+j] != p[j]:
                match = False
                break
        if match:
            occurrences.append(i)
    return occurrences, num_char_comp, num_alignmets_tried

p = "GGCGCGGTGGCTCACGCCTGTAATCCCAGCACTTTGGGAGGCCGAGG"

print(naive_with_counts(p,genome))