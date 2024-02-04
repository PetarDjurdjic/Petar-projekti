numDays = int(input("How many days temperature?: "))
total = 0
temp = []
for i in range(numDays):
    nextDay = int(input(f"Day {str(i+1)}'s high temperature: "))
    temp.append(nextDay)
    total = temp[i]

average = round(total/numDays,2)
print(f"Average: {str(average)}")


above = 0
for i in temp:
    if i > average:
        above +=1
print(f"{str(above)} day(s) above average")