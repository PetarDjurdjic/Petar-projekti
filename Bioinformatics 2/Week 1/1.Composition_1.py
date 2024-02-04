def Composition(Text,k):
    kmers = []
    for i in range(len(Text) - k +1):
        kmers.append(Text[i:i+k])
    return kmers

k = 3
Text = "1011100010"
result = (Composition(Text,k))
print(" ".join(result))