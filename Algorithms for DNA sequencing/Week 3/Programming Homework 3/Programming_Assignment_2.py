def readGenome(filename):
    genome = ""
    with open(filename, "r") as f:
        for line in f:
            if not line[0] == ">":
                genome += line.rstrip()
    return genome

genome = readGenome("chr1.GRCh38.excerpt.fasta")
genome[:100]


def approximate_match(p, t):
    # Create distance matrix
    D = []
    for i in range(len(p) + 1):
        D.append([0] * (len(t) + 1))

    # Initialize first row and column of matrix
    for i in range(len(p) + 1):
        D[i][0] = i
    for i in range(len(t) + 1):
        D[0][i] = 0

    # Fill in the rest of the matrix
    for i in range(1, len(p) + 1):
        for j in range(1, len(t) + 1):
            distHor = D[i][j - 1] + 1
            distVer = D[i - 1][j] + 1
            if p[i - 1] == t[j - 1]:
                distDiag = D[i - 1][j - 1]
            else:
                distDiag = D[i - 1][j - 1] + 1
            D[i][j] = min(distHor, distVer, distDiag)

    # Edit distance is the value in the bottom right corner of the matrix
    return min(D[-1])

p = "GATTTACCAGATTGAG"
t = genome

print(approximate_match(p,t))