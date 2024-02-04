dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

# def merge_dicts(dict1, dict2):
#     new_dict = {}
#     for key,value in dict1.items():
#         new_dict[key] =value
#     for key, value in dict2.items():
#         if key not in new_dict:
#             new_dict[key] = value
#         else:
#             new_dict[key] += value
#     return new_dict

# print(merge_dicts(dict1,dict2))

#-------------------------------------------------------------------

# 2

def merge_dict(dict1,dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        merged[key] = merged.get(key, 0) + value
    return merged

print(merge_dict(dict1,dict2))