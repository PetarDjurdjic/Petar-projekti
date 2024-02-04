def Score(Motifs):
    k = len(Motifs[0])
    consensus = (Consensus(Motifs))
    sum = 0
    for i in range(k):
        for j in range(len(Motifs)):
            if consensus[i] != Motifs[j][i]:
                sum +=1
    return sum
            
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

print(Score(Motifs))