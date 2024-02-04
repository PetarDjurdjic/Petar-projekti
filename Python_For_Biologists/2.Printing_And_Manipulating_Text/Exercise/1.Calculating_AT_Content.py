dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(dna_seq)
a_count = dna_seq.count("A")
t_count = dna_seq.count("T")
print(100*(a_count+t_count)/length)