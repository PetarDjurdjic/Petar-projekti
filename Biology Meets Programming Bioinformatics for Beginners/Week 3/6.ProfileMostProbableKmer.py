def ProfileMostProbableKmer(text, k, profile):
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


Text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
k = 5
Profile = {"A":[0.2, 0.2, 0.3, 0.2, 0.3],
"C":[0.4, 0.3, 0.1, 0.5, 0.1],
"G":[0.3, 0.3, 0.5, 0.2, 0.4],
'T':[0.1, 0.2, 0.1, 0.1, 0.2]}

print(ProfileMostProbableKmer(Text, k, Profile))