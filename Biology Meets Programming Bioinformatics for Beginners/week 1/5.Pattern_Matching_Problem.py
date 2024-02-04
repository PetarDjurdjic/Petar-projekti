# fill in your PatternMatching() function along with any subroutines that you need.
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    for i in range(len(Genome) - len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions


Pattern = "ATAT"
Genome = "GATATATGCATATACTT"

print(PatternMatching(Pattern, Genome))