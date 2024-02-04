# Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.

input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# 1

# def get_diagonal(input_tuple):
#     new_tuple = []
#     for i in range(0,len(input_tuple)):
#         new_tuple.append(input_tuple[i][i])
#     return tuple(new_tuple)

# print(get_diagonal(input_tuple))

#---------------------------------------------------

# 2

def get_diagonal(input_tuple):
    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))

print(get_diagonal(input_tuple))

