def hamming_distance(pattern1, pattern2):
    return sum(c1 != c2 for c1, c2 in zip(pattern1, pattern2))

motif_matrix = [
    "CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC",
    "GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC",
    "GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG"
]

options = [
    "TAGTTTC",
    "CGTGTAA",
    "GTAGGAA",
    "TCTGAAG",
    "GATGAGT",
    "ATAACGG"
]

k = 7

# Calculate Hamming distances
distances = {option: sum(min(hamming_distance(option, dna_string[i:i+k]) for i in range(len(dna_string) - k + 1)) for dna_string in motif_matrix) for option in options}

# Find the minimum distance
min_distance = min(distances.values())

# Select options with the minimum distance
median_strings = [option for option, distance in distances.items() if distance == min_distance]

print("Median string(s):", median_strings)
