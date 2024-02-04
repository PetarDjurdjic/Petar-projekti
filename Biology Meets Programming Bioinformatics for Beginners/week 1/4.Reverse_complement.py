# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    rev_comp = Reverse(Pattern)
    rev_comp = Complement(rev_comp)
    return rev_comp

# Copy your Reverse() function here.
def Reverse(Pattern):
    rev=""
    for i in Pattern:
        rev = i + rev
    return rev

# Copy your Complement() function here.
def Complement(Pattern):
    dna_complement = ""
    for i in Pattern:
        if i == "A":
            dna_complement += "T"
        elif i == "T":
            dna_complement += "A"
        elif i == "G":
            dna_complement += "C"
        else:
            dna_complement += "G"
    return dna_complement




Pattern = "GATTACA"
print(ReverseComplement(Pattern))