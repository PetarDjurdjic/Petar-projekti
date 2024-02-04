# ERR037900_1.first1000.fastq
import matplotlib.pyplot as plt

def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()
            seq = fh.readline().rstrip()
            fh.readline()
            qual = fh.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities

seqs, quals = readFastq("ERR037900_1.first1000.fastq")
print(seqs[:5])
print(quals[:5])

def phred33ToQ(qual):
    return ord(qual) - 33
print(phred33ToQ("#"))
print(phred33ToQ("J"))

def createHist(qualities):
    hist = [0] * 50
    for qual in qualities:
        for phred in qual:
            q = phred33ToQ(phred)
            hist[q] +=1
    return hist

h = createHist(quals)
print(h)


plt.bar(range(len(h)), h)
plt.show()





