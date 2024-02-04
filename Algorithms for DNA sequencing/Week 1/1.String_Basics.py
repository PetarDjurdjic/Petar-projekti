seq = "ACGT"
print(seq[1])

print()
print("LENGTH:")
print(len(seq))

e = ""
print(len(e))

print()
print("CONCATENATE:")
seq1 = "CCAA"
seq2 = "GGTT"
print(seq1 + seq2)

print()
print("CONCATENATE:")
new = ""
seqs = ["A", "C", "G", "T"]
print(new.join(seqs))
print(",".join(seqs))

print()
print("RANDOM:")
import random
print(random.choice("ACGT"))
print()
print("RANDOM SAME BEHAVIOUR:")
random.seed(6)
print(random.choice("ACGT"))


print()
print("RANDOM:")
seq = ""
for _ in range(10):
    seq +=random.choice("ACTG")
print(seq)

print()
print("RANDOM 2:")
seq_temp = "".join([random.choice('ACGT') for _ in range(10)])
print(seq_temp)
print(type(seq_temp))

print()
print("SLICE:")
print(seq_temp[1:3])
print(seq_temp[:3])
print(seq_temp[0:3])
print(seq_temp[-3])