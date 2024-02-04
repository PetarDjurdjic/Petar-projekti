string_dict = """0: 3
1: 0
2: 1 6
3: 2
4: 2
5: 4
6: 5 8
7: 9
8: 7
9: 6"""


my_dict = {int(key) : [int(val) for val in values.split()] if " " in values else int(values) for key, values in (line.split(":") for line in string_dict.split("\n") if line)}

print(my_dict)


# my_dict = {}
# lines = string_dict.split("\n")
# # print(lines)
# for line in lines:
#     parts = line.split(":")
#     # print(parts)
#     key = int(parts[0].strip())
#     # print(key)
#     values = [int(val.strip()) for val in parts[1].split()]
#     # print(values)
#     my_dict[key] = values if len(values) > 0 else None
#
# print(my_dict)


