# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def ApproximatePatternCount(Pattern, Text, d):
    count = 0
    for i in range(len(Text) - len(Pattern) +1):
        mm = hammingDistance(Text[i:i+len(Pattern)], Pattern)
        if mm <= d:
            count +=1
    return count

def hammingDistance(Text,Pattern):
    mm = 0
    for i in range(len(Text)):
        if Text[i] != Pattern[i]:
            mm +=1
    return mm


# ### DO NOT MODIFY THE CODE BELOW THIS LINE ###
# import sys
# lines = sys.stdin.read().splitlines()
# print(ApproximatePatternCount(lines[0],lines[1],int(lines[2])))

Pattern = "GAGG"
Text = "TTTAGAGCCTTCAGAGG"
d = 2
print(ApproximatePatternCount(Pattern,Text, d))