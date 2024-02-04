def naive_2mm(p,t):
    occurrences = []
    for i in range(len(t) - len(p) +1):
        mm = 0
        match = True
        for j in range(len(p)):
            if t[i+j] != p[j]:
                mm +=1
                if mm > 2:
                    match = False
                    break
        if match:
            occurrences.append(i)
    return occurrences