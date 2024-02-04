# Input: A dictionary Probabilities, where keys are k-mers and values are the probabilities of these k-mers (which do not necessarily sum up to 1)
# Output: A normalized dictionary where the probability of each k-mer was divided by the sum of all k-mers' probabilities
def Normalize(Probabilities):
    # your code here
    sum = 0
    for value in Probabilities.values():
        sum += value
    for key,value in Probabilities.items():
        Probabilities[key] = value/sum
    return Probabilities



Probabilities = {"1": 0.15, "2": 0.6, "3":0.225, "4": 0.225, "5":0.3}
# Probabilities = {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}
print(Normalize(Probabilities))