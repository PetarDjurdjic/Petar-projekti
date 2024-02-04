# Pitfalls and ways to avoid them

myList = [2,4,3,1,5,7]


# myList = myList.sort()
# print(myList)



# myList.append(10) #1

# myList = myList + [10] #2

# myList.append([10]) #3

# print(myList)



orig = myList [:]
myList.sort()
print(orig)
print(myList)
