# Longest common prefix


def longestCommonPrefix(s1,s2):
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i +=1
    return s1[:i]

print(longestCommonPrefix("ACCATGT","ACCAGAC"))

def match(s1,s2):
    if not len(s1) == len(s2):
        return False
    for i in range(len(s1)):
        if not s1[i] == s2[i]:
            return False
    return True

print(match("ATGCT", "ATGCT"))

# Built in method ==
print("ATGCT" == "ATGCT")


# Reverse complement


def reverseComplement(s):
    complement = {"A": "T", "C": "G", "G": "C", "T": "A"}
    rev_comp = ""
    for base in s:
        rev_comp = complement[base] + rev_comp
    return rev_comp

print(reverseComplement("AACGGTAAAACCCC"))
