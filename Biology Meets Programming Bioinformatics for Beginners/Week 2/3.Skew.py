def SkewArray(Genome):
    skew_list = [0]
    skew_sum = 0
    for i in Genome:
        if i == "G":
            skew_sum +=1
            skew_list.append(skew_sum)
        elif i == "C":
            skew_sum -=1
            skew_list.append(skew_sum)
        else:
            skew_list.append(skew_sum)
    return " ".join(map(str, skew_list))


Genome = "GATACACTTCCCGAGTAGGTACTG"
print(SkewArray(Genome))