def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {}
    # insert your code here
    for symbol in "ACGT":
        count[symbol] = [1] * k

    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1

    return count


Motifs = ["AACGTA",
'CCCGTT',
'CACCTT',
'GGATTA',
'TTCCGG']

print(CountWithPseudocounts(Motifs))