shoppingList = ["Milk", "Cheese", "Butter"]

print(shoppingList[0])

print("Milk" in shoppingList)
print("Bread" in shoppingList)

print()

for i in shoppingList:
    print(i)


print()

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + "+"
    print(shoppingList)
    print(shoppingList[i])