## Define a function to count the frequency of words in a given list of words.



words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 

# 1

# def count_word_frequency(list):
#     word_count= {}
#     for i in list:
#         if i not in word_count:
#             word_count[i] = 1
#         else:
#             word_count[i] += 1
#     return word_count

# print(count_word_frequency(words))

#------------------------------------------------------------

# 2

def count_word_frequency(list):
    word_count = {}
    for i in list:
        word_count[i] = word_count.get(i,0) +1
    return word_count

print(count_word_frequency(words))