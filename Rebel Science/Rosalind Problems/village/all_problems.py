# import this



# === Variables and some Arithmetic ===

a = 820
b = 857
# print(f"{a}^2 + {b}^2 = {a**2 + b**2}")



# === Strings and Lists ===

wordOneStartPos = 92
wordOneEndPos = 102

wordTwoStartPos = 173
wordTwoEndPos =183

txtStr = "MFualduHZeB0ap3f0xt62APiWUAVcyfSoNAJSHFIW4NwEvqKLkpjVaPDmFxmyzMvV2VT4SE0aQ1pB93JOjbbJonLsB0YLimnodromusP3w19n1YgYmuBE7eK1mcTG4WCD57zPls12wOMziCO9bSqGBX9OIRJTPFfgYfBsK1zBl6jafalcinellusV5z27WA68mHJwQK."

# print(f"{txtStr[wordOneStartPos:wordOneEndPos+1]} {txtStr[wordTwoStartPos:wordTwoEndPos+1]}")



# === Conditions and Loops

startPos = 4163
endPos = 8866
result = 0

# for x in range(startPos,endPos+1):
#     if x % 2 != 0:
#         result +=x


result = sum([x for x in range(startPos, endPos+1) if x%2 !=0])
# print(result)






# === Working with Files ===

import os
print(os.getcwd())

outputFile = []
with open("/Users/petar/Desktop/Petar-projekti/Rebel Science/Rosalind Problems/village/input.txt", "r") as f:
    outputFile = [line for pos, line in enumerate(f.readlines()) if pos%2 != 0]

print(outputFile)

with open("/Users/petar/Desktop/Petar-projekti/Rebel Science/Rosalind Problems/village/out.txt", "w") as f:
    f.write(''.join([line for line in outputFile]))





# === Dictionaries ===

txtStr = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

# Generic approach:


wordCountDict = {}
for word in txtStr.split(" "):
    if word in wordCountDict:
        wordCountDict[word] += 1
    else:
        wordCountDict[word] = 1


for key, value in wordCountDict.items():
    print(key,value)
# print(txtStr.split(" "))

# Optimized pythonic


from collections import Counter
wordCountDict = Counter(txtStr.split(" "))
