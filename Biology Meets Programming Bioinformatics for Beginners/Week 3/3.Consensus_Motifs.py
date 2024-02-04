def Consensus(Motifs):

    k = len(Motifs[0])
    count = Count(Motifs)

    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus


def Count(Motifs):
    count = {} 
    k = len(Motifs[0])
    t = len(Motifs)

    
    for symbol in "ACGT":
        count[symbol] = [0] * k

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



print(Consensus(Motifs))