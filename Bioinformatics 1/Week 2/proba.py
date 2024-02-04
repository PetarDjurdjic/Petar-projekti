def neighbors(pattern, d):
    nucleotides = ['A', 'C', 'G', 'T']
    count = 0
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return nucleotides
    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)
    for neighbor in suffix_neighbors:
        if hamming_distance(pattern[1:], neighbor) < d:
            for nuc in nucleotides:
                neighborhood.add(nuc + neighbor)
        else:
            neighborhood.add(pattern[0] + neighbor)
    return neighborhood

def hamming_distance(p, q):
    hd = 0
    if len(q) == len(p):
        for i in range(len(p)):
            if p[i] != q[i]:
                hd += 1
    else:
        print("Lengths are not of equal length.")
    return hd


pattern = "TGCAT"
d = 2
print(neighbors(pattern, d))