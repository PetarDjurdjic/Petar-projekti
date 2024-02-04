def frequency_table(genome, k):
    freq_map = {}
    for i in range(len(genome) - k +1):
        if genome[i:i+k] not in freq_map:
            freq_map[genome[i:i+k]] = 1
        else:
            freq_map[genome[i:i + k]] +=1
    return freq_map

def pattern_count(t,p):
    count = 0
    for i in range(len(t)-len(p)+1):
        if t[i:i+len(p)] == p:
            count +=1
    return count

def frequent_words(genome, k):
    frequent_patterns = []
    counts = []
    for i in range(len(genome)-k+1):
        pattern = genome[i:i+k]
        counts.append(pattern_count(genome, pattern))
    maxCount = max(counts)
    for i in range(len(genome) - k+1):
        if counts[i] == maxCount:
            frequent_patterns.append(genome[i:i+k])
        else:
            continue
    unique_patterns = list(set(frequent_patterns))
    result_string = " ".join(unique_patterns)
    return result_string


genome = "ACGTGGCATCCAGCGTGCGAGTACATACAGCGTGCTTGAGGTCGTTGAGGTCGTTGAGGTCGGAGTACATAGAGTACATAGAGTACATACAGCGTGCGAGTACATACGCCGGATCAGCGTGCCGCCGGATCGCCGGATCGCCGGATTTGAGGTCGCAGCGTGCCAGCGTGCGAGTACATAGAGTACATACAGCGTGCGAGTACATAACGTGGCATCGAGTACATACGCCGGATCAGCGTGCTTGAGGTCGTTGAGGTCGACGTGGCATCGAGTACATAACGTGGCATCCGCCGGATCAGCGTGCTTGAGGTCGCGCCGGATCGCCGGATACGTGGCATCGAGTACATACGCCGGATACGTGGCATCCAGCGTGCTTGAGGTCGGAGTACATATTGAGGTCGCAGCGTGCCAGCGTGCCAGCGTGCACGTGGCATCCAGCGTGCTTGAGGTCGTTGAGGTCGTTGAGGTCGCGCCGGATCAGCGTGCGAGTACATATTGAGGTCGCAGCGTGCTTGAGGTCGCAGCGTGCGAGTACATAGAGTACATATTGAGGTCGCAGCGTGCACGTGGCATCCAGCGTGCCGCCGGATGAGTACATACGCCGGATACGTGGCATCACGTGGCATCCGCCGGATACGTGGCATCTTGAGGTCGCAGCGTGCCAGCGTGCGAGTACATAACGTGGCATCGAGTACATAACGTGGCATCCAGCGTGCTTGAGGTCGCGCCGGATTTGAGGTCGCGCCGGATGAGTACATAACGTGGCATCCAGCGTGCTTGAGGTCGCAGCGTGCACGTGGCATCCAGCGTGCCGCCGGATACGTGGCATCCGCCGGATCGCCGGATGAGTACATATTGAGGTCGTTGAGGTCGACGTGGCATCACGTGGCATCGAGTACATACAGCGTGCCAGCGTGCGAGTACATACGCCGGATGAGTACATATTGAGGTCG"
k = 14
print(frequent_words(genome,k))

#------------------------------------------------------



def frequency_table(genome, k):
    freq_map = {}
    for i in range(len(genome) - k +1):
        if genome[i:i+k] not in freq_map:
            freq_map[genome[i:i+k]] = 1
        else:
            freq_map[genome[i:i + k]] +=1
    return freq_map

def pattern_count(t,p):
    count = 0
    for i in range(len(t)-len(p)+1):
        if t[i:i+len(p)] == p:
            count +=1
    return count

def max_map(freq_map):
    return max(freq_map.values())
def better_frequent_words(genome, k):
    frequent_patterns = []
    freq_map = frequency_table(genome,k)
    max_value = max_map(freq_map)
    for key, value in freq_map.items():
        if freq_map[key] == max_value:
            frequent_patterns.append(key)
    unique_patterns = list(set(frequent_patterns))
    result_string = " ".join(unique_patterns)
    return result_string

genome = "ACGTGGCATCCAGCGTGCGAGTACATACAGCGTGCTTGAGGTCGTTGAGGTCGTTGAGGTCGGAGTACATAGAGTACATAGAGTACATACAGCGTGCGAGTACATACGCCGGATCAGCGTGCCGCCGGATCGCCGGATCGCCGGATTTGAGGTCGCAGCGTGCCAGCGTGCGAGTACATAGAGTACATACAGCGTGCGAGTACATAACGTGGCATCGAGTACATACGCCGGATCAGCGTGCTTGAGGTCGTTGAGGTCGACGTGGCATCGAGTACATAACGTGGCATCCGCCGGATCAGCGTGCTTGAGGTCGCGCCGGATCGCCGGATACGTGGCATCGAGTACATACGCCGGATACGTGGCATCCAGCGTGCTTGAGGTCGGAGTACATATTGAGGTCGCAGCGTGCCAGCGTGCCAGCGTGCACGTGGCATCCAGCGTGCTTGAGGTCGTTGAGGTCGTTGAGGTCGCGCCGGATCAGCGTGCGAGTACATATTGAGGTCGCAGCGTGCTTGAGGTCGCAGCGTGCGAGTACATAGAGTACATATTGAGGTCGCAGCGTGCACGTGGCATCCAGCGTGCCGCCGGATGAGTACATACGCCGGATACGTGGCATCACGTGGCATCCGCCGGATACGTGGCATCTTGAGGTCGCAGCGTGCCAGCGTGCGAGTACATAACGTGGCATCGAGTACATAACGTGGCATCCAGCGTGCTTGAGGTCGCGCCGGATTTGAGGTCGCGCCGGATGAGTACATAACGTGGCATCCAGCGTGCTTGAGGTCGCAGCGTGCACGTGGCATCCAGCGTGCCGCCGGATACGTGGCATCCGCCGGATCGCCGGATGAGTACATATTGAGGTCGTTGAGGTCGACGTGGCATCACGTGGCATCGAGTACATACAGCGTGCCAGCGTGCGAGTACATACGCCGGATGAGTACATATTGAGGTCG"
k = 14
print(better_frequent_words(genome,k))