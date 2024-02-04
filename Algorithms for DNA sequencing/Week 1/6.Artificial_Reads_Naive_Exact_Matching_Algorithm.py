def readGenome(filename):
    genome = ""
    with open(filename, "r") as f:
        for line in f:
            if not line[0] == ">":
                genome += line.rstrip()
    return genome

genome = readGenome("phix.fa")

def naive(p,t):
    occurrences =[]
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if not t[i+j] == p[j]:
                match = False
                break
        if match:
            occurrences.append(i)
    return occurrences

t = "AGCTTAGATAGC"
p = "AG"

# print(naive(p,t))

import random
def generateReads(genome, numReads, readLen):
    """Generate reads from random position in the given genome."""

    reads = []
    for _ in range(numReads):
        start = random.randint(0, len(genome) - readLen) - 1
        reads.append(genome[start : start+readLen])
    return reads

reads = generateReads(genome, 100, 100)
numMatched = 0
for r in reads:
    matches = naive(r, genome)
    if len(matches) > 0:
        numMatched +=1
print("%d/ %d reads matched exactly" %(numMatched,len(reads)))

def readGenome(filename):
    genome = ""
    with open(filename, "r") as f:
        for line in f:
            if not line[0] == ">":
                genome += line.rstrip()
    return genome

genome = readGenome("phix.fa")

def naive(p,t):
    occurrences =[]
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if not t[i+j] == p[j]:
                match = False
                break
        if match:
            occurrences.append(i)
    return occurrences
def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()
            seq = fh.readline().rstrip()
            fh.readline()
            qual = fh.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities


phix_reads, _ = readFastq("SRR835775_1.first1000.fastq")

numMatched = 0
n = 0
for r in phix_reads:
    matches = naive(r,genome)
    n +=1
    if len(matches) > 0:
        numMatched += 1
print("%d / %d reads matched the genome!" %(numMatched, n))

