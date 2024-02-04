# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def contains_duplicate(nums):
    tempnums = []
    for i in nums:
        if i in tempnums:
            return True
        else:
            tempnums.append(i)

nums = [1,2,3,1]
print(contains_duplicate(nums))