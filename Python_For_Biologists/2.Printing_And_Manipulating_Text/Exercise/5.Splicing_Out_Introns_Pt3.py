dna_seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT" 
exon1 = dna_seq[0:62]
intron = dna_seq[62:90]
exon2 = dna_seq[91:]
print(exon1 + intron.lower() + exon2)
