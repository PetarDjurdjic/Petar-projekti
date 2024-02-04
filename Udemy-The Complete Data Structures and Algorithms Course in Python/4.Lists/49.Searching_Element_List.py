# Searching for an element in the list

my_list = [10,20,30,40,50,60,70,80,90]

# in operator

target = 90
# if target in my_list:
#     print(f"{target} is in the list")
# else:
#     print(f"{target} is NOT in the list")



# Linear search

def linear_search(p_list, p_target):
    for i, value in enumerate(p_list):
        if value == p_target:
            return i
    return -1

print(linear_search(my_list,target))