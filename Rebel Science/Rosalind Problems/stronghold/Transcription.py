def transcription(seq):
    # DNA -> RNA Transcription
    return seq.replace("T", "U")

seq = "TTCGGGAGGCTGGTGATAACGGGGACTTTTTGTGGCCGCAATGACCGATCCGAATGCTACGTTTCCATAGGATCCAGAGTCACAAGGATAACACCCATGGACAGCGTAATTGATCTTCCCTATATCCATGTTCGATGATGAGATTATGTTTTGGCGGTACGATAAGGGAGCTTTTCAAGAAGTGACGCGAATGCATTAATTCCTGGGTGGGCAGCGAGCGCCTAGTGAACATGTTTCAAAAAGGCACGGATAGTCCACACCGTCAAACTGCGTAGGTATTAACGGAAAGGCCTCGACCACATCAAGGAGAACTGATGACATTGACATTTTGGAGCCATGCATTACGTGACTGCATAAGATTCTTCCACACCTGTCAACGCGTAGTACCACCAATACAGCTGCCACTCACGGTTATTGATGGGCTATTTGGGCACGCTCTAGTAATCCAACAGCTTGTCTGATTAAATCGCAACTCTCCGATTGCCAATCACTAACTTGGTGTACGTAACGGCGGGTTCTCACCCCGGACGCGCGGGCCGCCGGATCTTAATGAGCATCACACCGAAGACAGCCCGGAGAGGTCCGCTCCGGCGCGCGTCCGGTACCAAGCTCGAAACTCTGACTGCGCCGTTCTAACTTGATCCCGAGAAGAATCGATGTGCACCAGCGGAACTAAGACGTTGCTGACTGCTGGTAGCACCGCCAATCGGCCTGAGGCCGTTGCTTTCTTTTTATAAGTGTATGTTAGGTGACACGTTAAACATCGCAAGAACTCCATGACAAGAAGGGGAGAGATCGCGCGAGTTCTCTGGTCTCCATTAACGCGCAGGCCTCCCGAGCTGACCCGAGACATGAGACGTATGAGGTTGCACAGGTGAACGTCACCGTAAATGTAACAGACCCGCAGTGGATT"
print(transcription(seq))