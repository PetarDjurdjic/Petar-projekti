## Define a function which takes as a parameter dictionary and returns a dictionary in which everse the key-value pairs are reversed.

# 1

my_dict = {'a': 1, 'b': 2, 'c': 3}
# def reverse_dict(my_dict):
#     new_dict = {}
#     for key, value in my_dict.items():
#         new_dict[value] = key
#     return new_dict

# print(reverse_dict(my_dict))

#------------------------------------------------

# 2

def reverse_dict(my_dict):
    return {value:key for key,value in my_dict.items()}

print(reverse_dict(my_dict))