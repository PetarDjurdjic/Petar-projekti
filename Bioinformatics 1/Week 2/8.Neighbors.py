def neighbors_count(pattern, d, count=0):
    nucleotides = ['A', 'C', 'G', 'T']
    if d == 0:
        return 1  # Only the pattern itself
    if len(pattern) == 1:
        return len(nucleotides)  # All possible single-nucleotide neighbors
    suffix_count = neighbors_count(pattern[1:], d)
    for neighbor in range(suffix_count):
        if hamming_distance(pattern[1:], nucleotides[neighbor]) < d:
            count += len(nucleotides)
        else:
            count += 1
    return count

def hamming_distance(p, q):
    if len(q) == len(p):
        return sum(1 for i, j in zip(p, q) if i != j)
    else:
        print("Lengths are not of equal length.")
        return None

pattern = "CAT"
d = 1
count = neighbors_count(pattern, d)
print("Total number of neighbors for pattern '{}': {}".format(pattern, count))
