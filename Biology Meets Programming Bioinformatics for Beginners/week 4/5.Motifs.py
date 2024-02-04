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

Dna =["TTACCTTAAC",
"GATGTCTGTC",
"ACGGCGTTAG",
"CCCTAACGAG",
"CGTCAGAGGT"]
Profile= {"A":[0.8, 0.0, 0.0, 0.2],
"C":[0.0, 0.6, 0.2, 0.0],
"G":[0.2, 0.2, 0.8, 0.0],
'T':[0.0, 0.2, 0.0, 0.8]}

print(Motifs(Profile, Dna))