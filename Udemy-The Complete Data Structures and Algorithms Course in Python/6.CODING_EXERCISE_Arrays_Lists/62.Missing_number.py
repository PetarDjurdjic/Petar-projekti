import numpy as np

def missing_number(arr, n):
    # Calculate the sum of first n natural numbers
    total = n * (n + 1) // 2
    
    # Calculate the sum of numbers in the array
    sum_arr = sum(arr)
    
    # Find the missing number by subtracting sum_arr from total
    missing = total - sum_arr
    
    return missing

arr = np.array([1,2,3,4,6,], dtype = int)
n = 6
print(arr)


# print(missing_number(arr,n))
