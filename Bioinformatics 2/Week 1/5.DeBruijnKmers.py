def constructDeBruijn(Patterns):
    my_dict = {}
    for i in range(len(Patterns)):
        my_dict[i] = []
        if Patterns[i][:-1] not in my_dict:
            my_dict[Patterns[i][:-1]] = [Patterns[i][1:]]
        else:
            my_dict[Patterns[i][:-1]].append(Patterns[i][1:])
    for key, value in my_dict.items():
        if value:
            print(f"{key}: {' '.join(value)}")


Patterns = "000 001 011 111 110 101 010 100".split(" ")
constructDeBruijn(Patterns)
