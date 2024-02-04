def findClumps(text, k, L, t):
    patterns = []
    n = len(text)

    for i in range(n - L + 1):
        window = text[i:i + L]
        freqMap = frequency_table(window, k)

        for key, value in freqMap.items():
            if value >= t:
                patterns.append(key)

    patterns = list(set(patterns))  # Remove duplicates
    return patterns


def frequency_table(t, k):
    freq_map = {}
    n = len(t)

    for i in range(n - k + 1):
        pattern = t[i:i + k]
        if pattern not in freq_map:
            freq_map[pattern] = 1
        else:
            freq_map[pattern] += 1

    return freq_map


# Example usage:
text = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
k = 5
L = 50
t = 4

result = findClumps(text, k, L, t)
print(result)
