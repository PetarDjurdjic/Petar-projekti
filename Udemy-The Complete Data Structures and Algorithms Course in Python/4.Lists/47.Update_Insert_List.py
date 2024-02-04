myList = [1,2,3,4,5,6,7]
print(myList)

# Update an element

myList[2] = 33
print(myList)
myList[4] = 55
print(myList)


# Insert an element insert() method

myList.insert(0,11)
print(myList)
myList.insert(4,15)
print(myList)

# Append() method

myList.append(55)
print(myList)

# Extend() method

newList = [11,12,13,14]

myList.extend(newList)
print(myList)