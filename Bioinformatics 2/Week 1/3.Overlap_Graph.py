def overlap(pattern):
    my_dict = {}
    for i in pattern:
        my_dict[i] = []
        for j in pattern:
            if i[1:] == j[:-1]:
                my_dict[i].append(j)

    for key, value in my_dict.items():
        if value:
            print(f"{key}: {' '.join(value)}")

pattern = "ATGCG GCATG CATGC AGGCA GGCAT GGCAC".split(" ")
overlap(pattern)


# def overlap(pattern):
#     my_dict = {}
#     for i in pattern:
#         my_dict[i] = []
#         for j in pattern:
#             if i[1:] == j[:-1]:
#                 my_dict[i].append(j)
#
#     for key, value in my_dict.items():
#         if value:
#             print(f"{key}: {' '.join(value)}")
#
# pattern = "ATGCG GCATG CATGC AGGCA GGCAT GGCAC".split(" ")
# overlap(pattern)
