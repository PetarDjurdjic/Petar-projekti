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

t = "AAACATAGGATCAAC"
p = "AA"

print(*naive(p, t), sep=' ')
