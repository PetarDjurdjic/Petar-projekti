# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.


# 1


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# def tuple_elementwise_sum(t1,t2):
#     new_tuple = []
#     for i in range(0,len(t1)):
#         new_tuple.append(t1[i] + t2[i])
#     return tuple(new_tuple)   

# output_tuple = tuple_elementwise_sum(tuple1, tuple2)
# print(output_tuple)  # Expected output: (5, 7, 9)

#------------------------------------------------------------

# 2
def tuple_elementwise_sum(t1,t2):
    if len(t1) != len(t2):
        raise ValueError("Input tuples must have the same length")
    result = tuple(a+b for a,b in zip(t1,t2))
    return result

print(tuple_elementwise_sum(tuple1,tuple2))