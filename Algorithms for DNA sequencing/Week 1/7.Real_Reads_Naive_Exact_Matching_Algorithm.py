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


phix_reads, _ = readFastq("ERR266411_1.first1000.fastq")

# numMatched = 0
# n = 0
# for r in phix_reads:
#     matches = naive(r,genome)
#     n +=1
#     if len(matches) > 0:
#         numMatched += 1
# print("%d / %d reads matched the genome!" %(numMatched, n))


# numMatched = 0
# n = 0
# for r in phix_reads:
#     r = r[:30]
#     matches = naive(r,genome)
#     n +=1
#     if len(matches) > 0:
#         numMatched += 1
# print("%d / %d reads matched the genome!" %(numMatched, n))


def reverseComplement(s):
    complement = {"A": "T", "C": "G", "G": "C", "T": "A", "N": "N"}
    rev_comp = ""
    for base in s:
        rev_comp = complement[base] + rev_comp
    return rev_comp


numMatched = 0
n = 0
for r in phix_reads:
    r = r[:30]
    matches = naive(r,genome)
    matches.extend(naive(reverseComplement(r), genome))
    n +=1
    if len(matches) > 0:
        numMatched += 1
print("%d / %d reads matched the genome!" %(numMatched, n))