def readGenome(filename):
    genome = ""
    with open(filename, "r") as f:
        for line in f:
            if not line[0] == ">":
                genome += line.rstrip()
    return genome


def naive_2mm(p,t):
    occurrences = []
    for i in range(len(t) - len(p) +1):
        mm = 0
        match = True
        for j in range(len(p)):
            if t[i+j] != p[j]:
                mm +=1
                if mm > 2:
                    match = False
                    break
        if match:
            occurrences.append(i)
    return occurrences

genome = readGenome("lambda_virus1.fa")
pattern = "TTCAAGCC"

reads = naive_2mm(pattern, genome)
# print(reads)

n = 0
for r in reads:
    n +=1
print(n)


