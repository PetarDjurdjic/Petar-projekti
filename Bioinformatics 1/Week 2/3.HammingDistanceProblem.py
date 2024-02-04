def hamming_distance(p,q):
    hd = 0
    if len(q) == len(p):
        for i in range(len(p)):
            if p[i] == q[i]:
                continue
            else:
                hd+=1
                continue
    else:
        print("Lengths are not of equal length.")
    return hd


p = "CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT"
q = "CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG"
print(hamming_distance(p,q))


