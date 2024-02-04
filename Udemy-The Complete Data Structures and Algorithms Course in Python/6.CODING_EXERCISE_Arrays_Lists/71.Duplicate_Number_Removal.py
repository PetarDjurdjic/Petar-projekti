templist = [1, 1, 2, 2, 3, 4, 5]

def remove_duplicates(list):
    new_list = []
    for i in list:
        if i in new_list:
            continue
        else:
            new_list.append(i)
    return new_list

print(remove_duplicates(templist))