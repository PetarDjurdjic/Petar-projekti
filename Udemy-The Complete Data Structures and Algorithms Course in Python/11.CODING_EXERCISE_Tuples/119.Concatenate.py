# Write a function that takes a tuple of strings and concatenates them, separating each string with a space.

input_tuple = ('Hello', 'World', 'from', 'Python')

# 1

# def concatenate_strings(input_tuple):
#     delimiter = "-"
#     new_string = delimiter.join(input_tuple)
#     return new_string
    
# output_string = concatenate_strings(input_tuple)
# print(output_string)  

#--------------------------------------------------------------------

# 2

def concatenate_strings(input_tuple):
    return " ".join(input_tuple)

print(concatenate_strings(input_tuple))

