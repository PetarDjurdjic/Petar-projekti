# Write a program to find all pairs of integers whose sum is equal to a given number.

# def findPairs(nums, target):
#      for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] == nums[j]:
#                 continue
#             elif nums[i] + nums[j] == target:
#                 print(i,j)
                   
                

# mylist = [2,6,3,9,11,6]
# findPairs(mylist,9)



def two_sums(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement],i]
        else: 
            seen[num] = i

nums = [2,7,11,15,2,4,5]
target = 9
indices = two_sums(nums,target)
print(f"Indices of the two numbers are: {indices}")
        

        
