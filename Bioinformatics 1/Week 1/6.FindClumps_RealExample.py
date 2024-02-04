def read_genome(file_path):
    with open(file_path, 'r') as file:
        return file.read()

file_path = "Ecoli_genome.txt"
text = read_genome(file_path)

def findClumps(text, k, L, t):
    patterns = []
    n = len(text)
    index = 0
    for i in range(n-L+1):
        window = text[i:i+L]
        freqMap = frequency_table(window, k)
        for key,value in freqMap.items():
            if freqMap[key] >= t:
                patterns.append(key)
    unique_patterns = list(set(patterns))
    for i in unique_patterns:
        index +=1
    return index

def frequency_table(t, k):
    freq_map = {}  # empty map


    for i in range(len(t) - k + 1):
        pattern = t[i:i + k]
        if pattern not in freq_map:
            freq_map[pattern] = 1
        else:
            freq_map[pattern] += 1

    return freq_map



k = 9
L = 500
t = 3
print(findClumps(text, k, L, t))