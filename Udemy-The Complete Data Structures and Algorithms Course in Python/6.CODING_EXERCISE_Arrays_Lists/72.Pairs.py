# Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

temp_list=[2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target = 7

# def findPairs(list,target):
#     pairs = []
#     for i, num in enumerate(list):
#         complement = target - num
#         if complement in list[i+1:]:
#             pairs.append(f"{num}+{complement}")
#         else:
#             continue
#     return pairs

# print(findPairs(temp_list,target))


#-----------------------------------------------------------

def findPairs(nums,target):
    result = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                result.append(f"{nums[i]}+{nums[j]}")
    return result
print(findPairs(temp_list,target))
