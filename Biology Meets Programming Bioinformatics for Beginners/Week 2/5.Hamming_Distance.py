def hammingDistance(text,pattern):
    mm = 0
    for i in range(len(text)):
        if text[i] != pattern[i]:
            mm +=1
    return mm

text = "CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG"
pattern = "ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT"
print(hammingDistance(text,pattern))