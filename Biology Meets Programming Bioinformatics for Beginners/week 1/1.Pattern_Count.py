def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i + len(Pattern)] == Pattern:
            count += 1
    return count


Text = "GACCATCAAAACTGATAAACTACTTAAAAATCAGT"
Pattern = "AAA"

print(PatternCount(Text, Pattern))

print(True or not False and False)