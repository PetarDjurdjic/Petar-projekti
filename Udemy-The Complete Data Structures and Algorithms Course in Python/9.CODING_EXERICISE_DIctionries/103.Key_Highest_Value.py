# Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.


# 1

my_dict = {'a': 5, 'b': 9, 'c': 2}
# def max_value_key(my_dict):
#     tmp_value= 0
#     tmp_key = " "
#     for i, j in my_dict.items():
#         if j > tmp_value:
#             tmp_value = j
#             tmp_key = i
#         else:
#             continue
#     return tmp_key


# print(max_value_key(my_dict))

#---------------------------------------------------

# 2

def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)

print(max_value_key(my_dict))