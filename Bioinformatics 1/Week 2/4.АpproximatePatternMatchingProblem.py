def approximate_matching(t,p,d):
    occurrences = []
    for i in range(len(t) - len(p)+1):
        mismatches = 0
        for j in range(len(p)):
            if t[i+j] != p[j]:
                mismatches +=1
                if mismatches >d:
                    break
        else:
            occurrences.append(i)
    return occurrences


t = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
p = "ATTCTGGA"
k = 3
print(*approximate_matching(t,p,k))

