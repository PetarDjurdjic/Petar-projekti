import random

def WeightedDie(Probabilities):
    p = random.uniform(0, 1)
    cumulative_prob = 0

    for kmer, probability in Probabilities.items():
        cumulative_prob += probability
        if p <= cumulative_prob:
            return kmer, p



Probabilities = {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25}
print(WeightedDie(Probabilities))