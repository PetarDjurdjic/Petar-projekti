# def read_genome(file_path):
#     with open(file_path, 'r') as file:
#         return file.read().strip()
#
# file_path = "MinSkew.txt"
# genome = read_genome(file_path)
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
    return [str(i) for i, j in enumerate(skewedList) if j == min(skewedList)]


genome = "GATACACTTCCCGAGTAGGTACTG"
result = skew(genome)
print(*result)
#
# values = {"A": 0,
#               "T": 0,
#               "G": +1,
#               "C": -1}
#
# result = values["C"]
# print(result)