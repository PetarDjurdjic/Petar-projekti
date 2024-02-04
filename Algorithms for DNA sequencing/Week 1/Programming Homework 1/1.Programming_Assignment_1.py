def readGenome(filename):
    genome = ""
    with open(filename, "r") as f:
        for line in f:
            if not line[0] == ">":
                genome += line.rstrip()
    return genome

genome = readGenome("lambda_virus1.fa")

def naive(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                match = False
                break
        if match:
            occurrences.append(i)  # all chars matched; record
    return occurrences


def reverseComplement(s):
    complement = {"A": "T", "C": "G", "G": "C", "T": "A", "N": "N"}
    rev_comp = ""
    for base in s:
        rev_comp = complement[base] + rev_comp
    return rev_comp

def naive_with_rc_first(pattern, genome):
    """First, implement a version of the naive exact matching algorithm that is strand-aware.
    That is, instead of looking only for occurrences of P in T, additionally look for occurrences of the reverse
    complement of P in T. If P is ACT, your function should find occurrences of both ACT and its reverse complement AGT in T."""
    occurrences = naive(pattern, genome)
    more_occurenences = naive(reverseComplement(pattern), genome)
    return occurrences + more_occurenences

reads = naive_with_rc_first("ACCT", genome)


n = 0
for r in reads:
    n +=1
print(n)