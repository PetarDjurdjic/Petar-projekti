# from itertools import product
#
# def HammingDistance(pattern1, pattern2):
#     # Calculate the Hamming distance between two patterns
#     return sum(c1 != c2 for c1, c2 in zip(pattern1, pattern2))
#
# def Neighbors(pattern, d):
#     # Generate all k-mers within Hamming distance d from the given pattern
#     nucleotides = 'ACGT'
#     if d == 0:
#         return {pattern}
#     if len(pattern) == 1:
#         return set(nucleotides)
#     neighbors = set()
#     suffix_neighbors = Neighbors(pattern[1:], d)
#     for neighbor in suffix_neighbors:
#         if HammingDistance(pattern[1:], neighbor) < d:
#             for nucleotide in nucleotides:
#                 neighbors.add(nucleotide + neighbor)
#         else:
#             neighbors.add(pattern[0] + neighbor)
#     return neighbors
#
# def FrequentWordsWithMismatches(Text, k, d):
#     frequent_patterns = set()
#     close = {}
#     frequency_array = [0] * (4 ** k)
#
#     for i in range(len(Text) - k + 1):
#         pattern = Text[i:i+k]
#         neighborhood = Neighbors(pattern, d)
#         for neighbor in neighborhood:
#             index = PatternToNumber(neighbor)
#             close[index] = 1
#             frequency_array[index] += 1
#
#     max_count = max(frequency_array)
#     for i in range(4 ** k):
#         if frequency_array[i] == max_count:
#             pattern = NumberToPattern(i, k)
#             frequent_patterns.add(pattern)
#
#     return frequent_patterns
#
# def PatternToNumber(pattern):
#     # Convert a DNA pattern to a numerical value
#     symbol_to_number = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
#     if not pattern:
#         return 0
#     symbol = pattern[-1]
#     prefix = pattern[:-1]
#     return 4 * PatternToNumber(prefix) + symbol_to_number[symbol]
#
# def NumberToPattern(number, k):
#     # Convert a numerical value to its corresponding DNA pattern
#     number_to_symbol = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
#     if k == 1:
#         return number_to_symbol[number]
#     prefix_index = number // 4
#     r = number % 4
#     symbol = number_to_symbol[r]
#     prefix_pattern = NumberToPattern(prefix_index, k - 1)
#     return prefix_pattern + symbol
#
# # Example usage
# Text = "ATTCTTATAATTATTTTACTTGTTTTATTATTAGTTATTGTTATAGTTTTAATTTTATTATTATTACTTATAGTTATTTTAATTATTATAATAGTTCTTCTTATTATAGTTATAGTTATTATAGTTGTTATTATACTTCTTTTAATTGTTTTACTTGTTATTTTATTAATAGTTTTATTACTTCTTGTTATTATATTATTAATACTTGTTATAATAGTTATTATAATAATTTTATTAATTATTCTTCTTTTACTTATTATTATACTTTTACTTTTAGTTATAATACTTCTTATTCTTTTACTTGTTATTATAATATTAATATTATTA"
# k = 6
# d = 3
# result = FrequentWordsWithMismatches(Text, k, d)
# print(result)
#
#
#
#
#
#----------------------------------------------------------


def frequent_words_with_mismatches(text, k, d):
    patterns = []
    freq_map = {}
    n = len(text)

    def neighbors(pattern, d):
        nucleotides = ['A', 'C', 'G', 'T']
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
        if len(p) == len(q):
            for i in range(len(p)):
                if p[i] != q[i]:
                    hd += 1
        else:
            print("Lengths are not of equal length.")
        return hd

    for i in range(n - k + 1):
        pattern = text[i:i + k]
        pattern_neighbors = neighbors(pattern, d)
        for neighbor in pattern_neighbors:
            if neighbor not in freq_map:
                freq_map[neighbor] = 1
            else:
                freq_map[neighbor] += 1

    max_count = max(freq_map.values())
    patterns = [pattern for pattern, count in freq_map.items() if count == max_count]

    return patterns

# Example usage
text = "ACGTT"
k = 4
d = 2
result = frequent_words_with_mismatches(text, k, d)
print(result)
