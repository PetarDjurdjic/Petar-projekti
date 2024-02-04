# Given a list, write a function to get first, second best scores from the list. List may contain duplicates.

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
def first_second(myList):
    max1,max2 = 0,0
    for i in myList:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2:
            max2 = i
    return max1,max2

print(first_second(myList))
