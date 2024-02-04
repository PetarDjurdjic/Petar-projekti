
def revcomp(t):
    complements = {"A": "T",
                   "C": "G",
                   "G": "C",
                   "T": "A"}
    rev = ""
    for i in t:
        rev +=complements[i]
    return rev[::-1]

t ="GATTACA"
print(revcomp(t))