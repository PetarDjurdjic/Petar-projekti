

def hammingDistance(pattern1,pattern2):
    countD = 0
    if len(pattern1) != len(pattern2):
        print("Lengths are not of the same size")
    else:
        for i in range(len(pattern1)):
            if pattern1[i] != pattern2[i]:
                countD +=1
    return countD

def approximatePatternCount(text,pattern,d):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        pattern_prim = text[i:i+len(pattern)]
        if hammingDistance(pattern, pattern_prim) <=d:
            count +=1
    return count

text = "CGTGACAGTGTATGGGCATCTTT"
pattern = "TGT"
d = 1

print(approximatePatternCount(text,pattern,d))