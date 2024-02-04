import random


def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {} 

    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)

    probabilities = Normalize(probabilities)

    return WeightedDie(probabilities)


def Normalize(Probabilities):
    # your code here
    sum = 0
    for value in Probabilities.values():
        sum += value
    for key,value in Probabilities.items():
        Probabilities[key] = value/sum
    return Probabilities

def Pr(Text, Profile):
    k = len(Text)
    profile = 1

    for i in range(k):
        symbol = Text[i]
        num = Profile[symbol][i]
        profile *= num

    return profile


def WeightedDie(Probabilities):
    p = random.uniform(0, 1)
    cumulative_prob = 0

    for kmer, probability in Probabilities.items():
        cumulative_prob += probability
        if p <= cumulative_prob:
            return kmer


text = "AAACCCAAACCC"
profile = {'A': [0.5, 0.1], 'C': [0.3, 0.2], 'G': [0.2, 0.4], 'T': [0.0, 0.3]}
k = 2
print(ProfileGeneratedString(text, profile, k))