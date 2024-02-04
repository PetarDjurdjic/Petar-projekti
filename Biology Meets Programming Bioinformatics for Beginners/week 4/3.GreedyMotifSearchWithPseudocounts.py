def Score(Motifs):
    consensus = Consensus(Motifs)
    k = len(consensus)
    t = len(Motifs)
    score = 0

    for j in range(k):
        for i in range(t):
            if Motifs[i][j] != consensus[j]:
                score += 1

    return score

def Count(Motifs):
    count = {}
    k = len(Motifs[0])

    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(1)

    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1

    return count

def Profile(Motifs):
    count = Count(Motifs)
    profile = {}

    k = len(Motifs[0])
    t = len(Motifs)
    
    for symbol in "ACGT":
        profile[symbol] = []
        for j in range(k):
            profile[symbol].append(count[symbol][j] / t)

    return profile

def Consensus(Motifs):
    profile = Profile(Motifs)
    consensus = ""

    k = len(Motifs[0])
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if profile[symbol][j] > m:
                m = profile[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol

    return consensus

def ProfileMostProbableKmer(Text, k, Profile):
    max_prob = -1
    most_probable = ""

    for i in range(len(Text) - k + 1):
        pattern = Text[i:i+k]
        prob = Pr(pattern, Profile)
        if prob > max_prob:
            max_prob = prob
            most_probable = pattern

    return most_probable

def Pr(Text, Profile):
    p = 1.0

    for i in range(len(Text)):
        symbol = Text[i]
        column = i

        p *= Profile[symbol][column]

    return p

def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    n = len(Dna[0])
    BestMotifs = [Dna[i][0:k] for i in range(t)]

    for i in range(n - k + 1):
        motifs = [Dna[0][i:i+k]]
        for j in range(1, t):
            profile = Profile(motifs[0:j])
            motifs.append(ProfileMostProbableKmer(Dna[j], k, profile))

        if Score(motifs) < Score(BestMotifs):
            BestMotifs = motifs

    return BestMotifs


k = 3 
t = 5
Dna = ["GGCGTTCAGGCA",
"AAGAATCAGTCA",
"CAAGGAGTTCGC",
"CACGTCAATCAC",
"CAATAATATTCG"]

print(GreedyMotifSearchWithPseudocounts(Dna, k, t))