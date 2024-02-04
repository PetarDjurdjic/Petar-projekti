import random

def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M

    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs



def RandomMotifs(Dna, k, t):
    motifs = []
    for i in range(t):
        rand_num = random.randint(0, len(Dna[i]) - k)
        motifs.append(Dna[i][rand_num: rand_num + k])
    return motifs



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

def Motifs(Profile, Dna):
    n = len(Dna[0])
    for key in Profile.keys():
        k = len(Profile[key])
    Motifs = []
    for i in range(len(Dna)):
        Motifs.append(ProfileMostProbablePattern(Dna[i], k, Profile))
    return Motifs   
    
def ProfileMostProbablePattern(text, k, profile):
    max = 0
    max_kmer = ""
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        prof_val = Pr(kmer,profile)
        if prof_val > max:
            max = prof_val
            max_kmer = kmer
        else:
            continue
    if max == 0:
        return text[0:0+k]
    else:
        return max_kmer
    
def Pr(Text, Profile):
    k = len(Text)
    profile = 1

    for i in range(k):
        symbol = Text[i]
        num = Profile[symbol][i]
        profile *= num

    return profile

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




Dna = ["TGACGTTC",
"TAAGAGTT",
"GGACGAAA",
"CTGTTCGC"]

t = len(Dna)
k = 3

print(RandomizedMotifSearch(Dna, k, t))