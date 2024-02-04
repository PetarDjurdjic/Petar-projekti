#1

# arr = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#     arr[i - 1] = arr[i]
# for i in range(0, 6): 
#     print(arr[i], end = " ")

#-------------------------------------------------------------------------
#2

# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50
# print(a)


#-------------------------------------------------------------------------
#3

# def f(value, values):
#     v = 1
#     values[0] = 44
# t = 3
# v = [1, 2, 3]
# f(t, v)
# print(t, v[0])

#-------------------------------------------------------------------------


# 4

# data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# def fun(m):
#     v = m[0][0]
 
#     for row in m:
#         for element in row:
#             if v < element: v = element
 
#     return v
# print(fun(data[0]))


#-------------------------------------------------------------------------

#5

# arr = [[1, 2, 3, 4],
#        [4, 5, 6, 7],
#        [8, 9, 10, 11],
#        [12, 13, 14, 15]]
# for i in range(0, 4):
#     print(arr[i].pop())


#-------------------------------------------------------------------------

#6 

# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
 
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'
 
# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
 
# print(sum)


