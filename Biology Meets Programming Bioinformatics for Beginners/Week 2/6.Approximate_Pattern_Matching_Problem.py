def ApproximatePatternMatching(Text, Pattern, d):
    positions = []
    for i in range(len(Text) - len(Pattern) +1):
        mm = hammingDistance(Text[i:i+len(Pattern)], Pattern)
        if mm <= d:
            positions.append(i)

    return positions

def hammingDistance(Text,Pattern):
    mm = 0
    for i in range(len(Text)):
        if Text[i] != Pattern[i]:
            mm +=1
    return mm

Pattern = "ATTCTGGA"
Text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
d = 3
print(ApproximatePatternMatching(Text, Pattern, d))