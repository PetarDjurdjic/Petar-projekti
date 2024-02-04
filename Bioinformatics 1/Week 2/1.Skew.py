def skew(genome):
    skewedList = []
    sum_value= 0
    skewedList = [sum_value]
    values = {"A": 0,
              "T": 0,
              "G": +1,
              "C": -1}
    for i in genome:
        sum_value += values[i]
        skewedList.append(sum_value)
    return skewedList

genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"
result = skew(genome)
print(*result)


