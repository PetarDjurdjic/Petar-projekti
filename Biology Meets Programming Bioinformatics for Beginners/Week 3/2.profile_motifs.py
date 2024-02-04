def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}

    for symbol in "ACGT":
        profile[symbol] = [0.0] * k

    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            profile[symbol][j] += 1/t

    return profile


Motifs = ["AACGTA",
'CCCGTT',
'CACCTT',
'GGATTA',
'TTCCGG']

print(Profile(Motifs))