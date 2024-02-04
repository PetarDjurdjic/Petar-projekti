# def repeatedSeq(s):
#     dict = {}
#     lst = set()
#     k = 10
#     for i in range(len(s) - k +1):
#         if s[i:i+k] not in dict:
#             dict[s[i:i+k]] = 1
#         else:
#             dict[s[i:i + k]] += 1
#             if dict[s[i:i + k]] >=2:
#                 lst.add(s[i:i + k])
#     return  lst
#
# s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# print(repeatedSeq(s))


def example_word_count():
    # This example question requires counting words in the example_string below.
    example_string = "Amy is 5 years old"

    # YOUR CODE HERE.
    # You should write your solution here, and return your result, you can comment out or delete the
    # NotImplementedError below.
    result = example_string.split(" ")
    return len(result)

    # raise NotImplementedError()

print(example_word_count())