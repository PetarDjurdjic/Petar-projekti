# Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

# 1

# def common_elements(tuple1, tuple2):
#     new_list = []
#     for i in tuple1:
#         if i in tuple2:
#             new_list.append(i)
#         else:
#             continue
#     return tuple(new_list)

# output_tuple = common_elements(tuple1, tuple2)
# print(output_tuple)  

#------------------------------------------------------

# 2

# def common_elements(t1,t2):
#     return tuple(i for i in tuple1 if i in tuple2)

# print(common_elements(tuple1,tuple2))

#--------------------------------------------------

# 3

def common_element(t1,t2):
    return tuple(set(t1) & set(t2))

print(common_element(tuple1, tuple2))