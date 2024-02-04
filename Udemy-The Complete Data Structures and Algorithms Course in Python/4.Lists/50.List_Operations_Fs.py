# List operations / Functions

# a = [1,2,3]
# b = [4,5,6]
# c = a + b
# print(c)


# * operator

a = [0,1]
a = a*4

print(a)


# len function

a = [0,1,2,3,4,5,6]
print(len(a))

# man i min
print(max(a))
print(min(a))

# sum
print(sum(a))


# total = 0
# count = 0

# while(True):
#     inp = input("Enter a number: ")
#     if inp == "done":
#         break
#     value = float(inp)
#     total = total + value
#     count +=1
#     average = total / count

# print(f"Average: {average}")


myList = []
while (True):
    inp = input("Enter a number: ")
    if inp == "done":
        break
    value = float(inp)
    myList.append(value)
    avg_list = (sum(myList) / len(myList))
print(f"Average: {avg_list}")    