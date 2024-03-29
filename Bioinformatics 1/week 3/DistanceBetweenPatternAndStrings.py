def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern)
    l = len(Dna)
    distance = 0
    for i in range(l):
        hamming_distance_min = float('inf')
        for j in range(len(Dna[i])-k+1):
            if hamming_distance_min > HammingDistance(Pattern,Dna[i][j:j+k]):
                hamming_distance_min = HammingDistance(Pattern,Dna[i][j:j+k])
        distance = distance + hamming_distance_min
    return distance


def HammingDistance(genome,pattern):
    mm = 0
    for i in range(len(genome)):
        if genome[i] != pattern[i]:
            mm +=1
    return mm


Dna = "ACCAAGGTCCGCCGTTCATCTGATGCGCAAGGCTTTGACCCGGTAGCGCTCGATTTTCGGGGTACCGGAGTAGATCTGGATCTCATGCAATCACGAAGA GCCCCGCTCCCATGTTTCGATACGTGGCCCATGGCAAAGAGGTATTTCATGGCCGCCCCATGCTTGGCATCCCCCGCTTGTCGTCAGAGCCAGGCGGCG TGGTTGAAGCTCACCTGTTGAGTCAATCGATACCGCCGCATGGTTCGACGGTTCTCGTGAATAGAATCTGTTTATACCTAGCGTAATACACGCCCCCAC TTGCGGTGATAGACTGTAGGTCGAGAACAACTAAACCGAAACACCACGTGCCGTGCCTGAGCGCGTATAACTGCAATCCCTGTCTGAATTTTCCATATG ACACGCTTTCTCCGAATAGGGGCAAACCGGCATTGAGAATAGAATACATATAGCGTCGGTATGGTCGACGTCAGACTTCCGTCCCTAACAATTCGATGA GATATGAGCATACGTACGAGGAACCTGGGAGTGCTACGGACTAATCTCGGTGCTCTTCAAGGCCATGTTGCGGCTGTGAGATCCACTATAAAATGCTGA GGTCAGTTAAACCAGCGTACTGGCGAGGATAAGCTGAGAAGGGCTTGATATATGCTTCAAGTGGAGCAAATCCTGCGACGTATGTTCTGTACTGGATAG TCAATACCATAAGCCAACGTCCTGTAATTAGATAAGTGGCAACGACGGTCGAGGCCTGGATGACTGATATAATTTCCGGTTTCCGCTTCCCACCAGCCG TTAGGCAATTTTTCAGTGTGTGTTTGCACTTGTCAACCATAGGCACCAAACCGCGATTCCTCTGGATTACGAAGGGCACACCTGATAGACGGATCCAAG AGAACACTTTAGCTAGTTCCCATAACTTGGGCTAGGTGAAGACAAGAGCTTACCCCGGCAGAGTGCAGCGAGTGACTGAAAGTTCATAAAGCATTAGAC TGGTCACCTCCTGCGGAGCTGCACTGTATAGTTAGGATCGACGGACCACTTGTAATTGGTAGTAATGAGGCTGCTTTTGTCGGCCTGACGCCTGTTGCT TTAGTGCTTTAGTATAACGATCTCCTGACATTTGACTTCGACATGCCTCGGGGGCCAACATTCACCTCGTAGCTGTCATATTCGTAAGTATGTTCGAAG TCCTAACGACCTGCTCCATCTTGTACGGGAACGCGTCTCGGTGAATGTCAGGAGTCTCTCGCCTAGTCTTCGGCAATCGGAAGGAATTCTTCTATGCCG CGTCCTGACAGGGCGGCCGTTAGAATAAGCATTATGAGACTCGCGCCTTCTAGGCGGGGCTTCCTCCTCCACCTGAGAATGCTATTTCGCAAATCGGGG GCCATCGGCGTTACTGTCGGTACTTGGATGCACATACTCACGACTTATCAAACTTATCGGAGAAAAGTTCTAGTTCAGCAGAGCGGTGGATTAATAGGT ACAACAGCGACTTACATGGCTTACGAGCTAGTAATAGTGACCATCTAGGACATCATGTAATGTACCTAAGTCTACAGCAATTAGGGTCGTATTATCCAA CACGGGGTCTGGCTGAGTTCTTAATGGGGGTTCAGGAACCATCGTCAGTTTTGTTGACTCCGTCTCGTCTCGGGCAATCATGTGGCCACACGTTAGTTC AGGATTCTCCCGCGAACAGGCAATGCTCAGTCAACAGCGTGAGACGACATCTAGTTCAAGTCAGTTTCACGAATTATTATAGGTCATGCGTTAGCTTAG ACAAGGGCGCACCTGGCTGGACAGAAACCATGCGTCGTGTAGATGTGGTTACCCCGAGTTGGGGAGGCGATTATCTATCAGGCCGGTGTTTACTACCGA GTGGCGTACAATGATCATGTTCGCCTATTCTGATGTCTGTGATACTACGCAACTGCATCTATATTAGACCTATCGGTATCTATCAGGGTAGACCTAGTG ATCACCCTGACATAGGTGATTCGAGTATTCAGCGGATCCTGAGAATATATGCGAGACCAGATTTAGAAGCCTACACGACGTGCACACGACTCCTGGTTG GATAACGGAATGCTGGCAACTACCGCCCACGATCATTATCTTGGCTCTATCGATCCGCGGCGTGTTATGCAACGGTCCGGCCCTCGCTCGAAAACGGAC TTGACCCGAGTTCGATGTCTGATGAAAAATCAGTGCACTCATTCCGTAACCAGGACCATAGGAGCAAGCATACGGCATCCCAGAATCTCGTCCGGAATG CGATCGTGGTGGTGGGTACAACAAATGGTGCCAGTGGAAGGATTAACTATGCCCCGAACGCCGAACGCAGCGAGTGCAGTTTAGAATACGAGGGAAGTA GGGTGGTATGCGTTTATCAAAGCCGGATTCACTGCTAGGGAATTGCTTGGGGTCACGGGCGCGTGGTGGCTCGTACGTTATCACCATTTGTACAACCCC ATGCTGTAGATAGGCCGCGCGAGCGCCCCCATTTGACATGGTAGTATAAAGCCAGACCGTATAGCGGAGCAAAGTGGAGTATCTCAGGGCGCAAGCGCT ATAAGGTCCGAAATCTGTAGTCAGAGTTAGGATGGTCAGTCAGGTTTGTTTTCGCCGTGATCGTGGGTATATTTAGTCAGGAGTTCCCTCGTAACTACT AGCCAGTGTTCGCGGGTTAACATCCGAGGTTGGCCGCGGGACTCTCCGCTATTATTCCCGGGCATATATCCACCGAAGGTGTCCACAGCGCTATAGGGG AACTTGCTGAGCCTCGCGTAAAACTGACCACATCATTTCGGGCGAAGTTGGAGCTAAGAACGGGGCTCCCTCCATGAAAGAAGACAAGGCCCCAAACTA GGGCTCGATGTACCCCCCCCGCTCAGGACTTAGATCTCTGAGCTGGCAGTCAGCTTAAGTGGTTGTGTGCCACACACTTATTAGGTACAGGGCGAGGCA TCTAGTTACGAAAATCTATCAGGTCTCCCTTATTAGTTCCCAGTGGGCCGGTATATACTGCAGCCAGTGCGTTGGGCTCAAGTAAAAGCCAGCAGAATG GACCGTTTCTCGTCCGTGTTCTACGGCTAGGCTATATGTGAGGTAGCTCCACCAATGCAGTTTGCAAGCCGGAATTCTCACGTGTGCACGACCTCATAA GAACTTTCTTAGCGGTAGTACACAGTAGGATATCTGTAGCTCGGTGCAATGTGGTATCTCTGGGTGCTACCTAATGCGATAGTGTGTCTTCCTGTCACT GACATACCACTTATACTCATTACACTCAACCAAAGTCGTCTGCGTACCACAGTCCCACAAGAGCTAGGCGAGCCTGGATCAAGTAACCCGAGCCCGATG CTAGGGTGGGTACGATGAGCTGTAAAGATGCCTAGGTCTCACGGAAAAGTGTGGCATGTTGTTTGCGCGGTACAATATATTCGGGTATTCAAAGTCAGA CTGGGACTTTCCGCACCACTGGCGGGGATTGAAGTGCAATGGATCATCATCGGCGACATCCAGACTCAACCGCAGCTAAGTAAAAAGGTGAATGCTAGG ATGCGGGTTTAAAATTTTATAAGTCTGCATCTACATAGCCCTATCGCACCGGTATGTTATAAACGCACGAATAAAGGACTCCGATGCCTACTAGCCTAC AGACCCGAGACCCGTTGCGCTTGCGAATCCAGCTTTTAGTATATTTTTTCGGATCCGTCGGTGGGATAACATCTGAACCACGCTTGTAGCACCGAAACA TTGATGCTGAGGCCCTCCCCTCCCGCTATCGCCTGGTTCCAGGCATACAAGGACTTCAGTAGAACCTGAAATCGGTGCCTGGACTTGGTCACAAAGTCT CTGAATAAAACTAAATATTGTGTTTCAGAACGCTTCACCACGTATCTCCGCTCCGCTGCTCTGTTGCTTTGGACTGACTGGGATACGGGAGCTATTCGC".split()
Pattern = "CTGATAA" 
print(DistanceBetweenPatternAndStrings(Pattern, Dna))

