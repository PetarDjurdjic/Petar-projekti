def ProfileWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {} 

    profile = CountWithPseudocounts(Motifs)
    for symbol in "ACGT":
        for i in range(k):
            profile[symbol][i] = profile[symbol][i] /(t+4)
    return profile


def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    count = {}

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
print(ProfileWithPseudocounts(Motifs))