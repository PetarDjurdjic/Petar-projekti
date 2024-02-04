def overlap(a,b,min_length=3):
    start = 0
    while True:
        start = a.find(b[:min_length], start)
        if start == -1:
            return 0
        if b.startswith(a[start:]):
            return len(a)-start
        start +=1

import itertools

def scs(ss):
    shortest_sup = None
    for ssperm in itertools.permutations(ss):
        sup = ssperm[0]
        for i in range(len(ss)-1):
            olen = overlap(ssperm[i],ssperm[i+1], min_length=1)
            sup += ssperm[i+1][olen:]
        if shortest_sup is None or len(sup) < len(shortest_sup):
            shortest_sup = sup
    return shortest_sup


def pick_maximum_overlap(reads,k):
    readA, readB = None, None
    best_olen = 0
    for a,b in itertools.permutations(reads,2):
        olen = overlap(a,b,min_length=k)
        if olen > best_olen:
            readA, readB = a,b
            best_olen = olen
    return readA, readB, best_olen

def greedy_scs(reads,k):
    read_a, read_b, olen = pick_maximum_overlap(reads,k)
    while olen > 0:
        reads.remove(read_a)
        reads.remove(read_b)
        reads.append(read_a + read_b[olen:])
        read_a, read_b, olen = pick_maximum_overlap(reads,k)
    return "".join(reads)

print(greedy_scs(["ABC", "BCA", "CAB"],2))

print(greedy_scs(["ABCD", "CDBC", "BCDA"],1))
print(scs(["ABCD", "CDBC", "BCDA"]))
