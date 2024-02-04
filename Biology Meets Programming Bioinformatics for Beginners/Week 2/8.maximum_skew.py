def maximumSkew(Genome):
    positions = [] 
    skew = SkewArray(Genome)
    min = sorted(skew)
    for i in range(len(skew)):
        if skew[i] == min[-1]:
            positions.append(i)  
    return positions


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
    return skew_list

genome = "GATACACTTCCCGAGTAGGTACTG"
print(maximumSkew(genome))
