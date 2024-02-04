# Write a function that calculates the sum and product of all elements in a tuple of numbers.

input_tuple = (1, 2, 3, 4)
# sum_result, product_result = sum_product(input_tuple)
# print(sum_result, product_result)  # Expected output: 10, 24

# 1


# def sum_result(input_tuple):
#     sum=0
#     for i in input_tuple:
#         sum+=i
#     return sum

# def product_result(input_tuple):
#     product = 1
#     for i in input_tuple:
#         product *= i
#     return product

# print(sum_result(input_tuple))
# print(product_result(input_tuple))



# 2

# def sum_product(input_tuple):
#     sum_result = sum(input_tuple)
#     product_result = 1
#     for i in input_tuple:
#         product_result *=i
#     return sum_result, product_result

# print(sum_product(input_tuple))

# 3 

def sum_product(input_tuple):
    sum_result = 0
    product_result = 1

    for num in input_tuple:
        sum_result +=num
        product_result *=num
    return sum_result, product_result

sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)

