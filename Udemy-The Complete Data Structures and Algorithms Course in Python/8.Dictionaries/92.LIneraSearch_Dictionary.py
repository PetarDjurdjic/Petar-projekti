myDict = {'name': 'Edy', 'age': 27, 'Address': 'London'}

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return "The value does not exist"


print(searchDict(myDict, 27))
