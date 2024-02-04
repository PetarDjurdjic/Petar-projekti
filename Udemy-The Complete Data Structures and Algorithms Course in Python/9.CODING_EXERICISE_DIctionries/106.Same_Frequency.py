# Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.


# 1

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
# def check_same_frequency(list1, list2):
#     counter1 = {}
#     counter2 = {}
#     for i in list1:
#         counter1[i] = counter1.get(i,0) +1
#     for i in list2:
#         counter2[i] = counter2.get(i,0) +1
#     return counter1 == counter2

# print(check_same_frequency(list1,list2))

#----------------------------------------------------------

def check_same_frequency(list1,list2):
    def counter_elements(list):
        counter = {}
        for i in list:
            counter[i] = counter.get(i,0)+1
        return counter
    return counter_elements(list1)== counter_elements(list2)

print(check_same_frequency(list1,list2))