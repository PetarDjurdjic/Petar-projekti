# Invoke-WebRequest -Uri https://d28rh4a8wq0iu5.cloudfront.net/ads1/data/ERR266411_1.for_asm.fastq -OutFile ERR266411_1.for_asm.fastq
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

seqs, quals = readFastq("SRR835775_1.first1000.fastq")

def findGCByReads(reads):
      gc = [0] * 100
      totals = [0] * 100

      for read in reads:
          for i in range(len(read)):
              if read[i] == "C" or read[i] == "G":
                  gc[i] +=1
              totals[i] +=1

      for i in range(len(gc)):
          if totals [i] > 0:
              gc[i] /=float(totals[i])

      return gc

gc = findGCByReads(seqs)
plt.plot(range(len(gc)), gc)
plt.show()

import collections
count = collections.Counter()
for seq in seqs:
    count.update(seq)
print(count)


