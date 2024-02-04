dna_seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
replacement1 = dna_seq.replace("A","t")
replacement2 = replacement1.replace("G", "c")
replacement3 = replacement2.replace("C", "g")
replacement4 = replacement3.replace("T", "a")
print(replacement4.upper())