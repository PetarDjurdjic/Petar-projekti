#Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

##1

# myList = [1, 2, 3, 4]
# def middle(myList):
#     newList=[]
#     for i, num in enumerate(myList):
#         if i == 0 or i == len(myList)-1:
#             continue
#         else:
#             newList.append(num)
#     return newList        

# print(middle(myList))

#--------------------------------------------------------------------

##2

myList = [1, 2, 3, 4]
def middle(lst):
    return lst[1:-1]

print(middle(myList))