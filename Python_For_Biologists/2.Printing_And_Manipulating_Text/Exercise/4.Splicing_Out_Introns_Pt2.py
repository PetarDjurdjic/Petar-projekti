dna_seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon = str(dna_seq[0:62]) + str(dna_seq[90:])
print(len(exon) / len(dna_seq))