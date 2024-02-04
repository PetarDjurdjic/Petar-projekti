def GenomePath(Pattern):
    genome = ""
    for i in range(len(Pattern)):
        if i == 0:
            genome += Pattern[i]
        else:
            genome += Pattern[i][-1]
    return genome



Pattern = " ".split(" ")
print(GenomePath(Pattern))