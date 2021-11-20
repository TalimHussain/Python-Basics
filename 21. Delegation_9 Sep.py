"Delegation"

"""
Delegation: It is a technique using which we can leave a scope to add new functionalities to 
a function in the future without changing it
"""

# x = 9
# y = x


# def func1():
#     print("This is func1")
#
# func1()
#
# print(func1)
#
# a = func1
# print(a)
#
# a()


"""
l = [5, 1, 6, 7, 0, 2, 3, 4, 9, 7]
l = [1, 5, 6, 7, 0, 2, 3, 4, 9, 7]
l = [0, 5, 6, 7, 1, 2, 3, 4, 9, 7]
l = [0, 1, 6, 7, 5, 2, 3, 4, 9, 7]
l = [0, 1, 5, 7, 6, 2, 3, 4, 9, 7]
l = [0, 1, 2, 7, 6, 5, 3, 4, 9, 7]
.
.
.
.
l = [0, 1, 2, 3, 4, 5, 6, 7, 7, 9]
"""


# def mySort(L):
 #     for i in range(len(L)):
#         for j in range(i+1, len(L)):
#             if L[i] > L[j]:
#                 L[i], L[j] = L[j], L[i]
#
# l = [5, 1, 6, 7, 0, 2, 3, 4, 9, 7]
# mySort(l)
# print(l)



# def mySort(L, key = None):
#     if key == None:
#         for i in range(len(L)):
#             for j in range(i+1, len(L)):
#                 if L[i] > L[j]:
#                     L[i], L[j] = L[j], L[i]
#
#     else:
#         for i in range(len(L)):
#             for j in range(i+1, len(L)):
#                 if key(L[i]) > key(L[j]):
#                     L[i], L[j] = L[j], L[i]
#
# def inverse(e):
#     return 1/e
#
# def square(e):
#     return e**2

# l = [5, 1, 6, 7, 8, 0, 2, 3, 4, 9, 7]
# mySort(l, key = inverse)
# print(l)

# l = [5, -1, 6, 7, -8, 2, -3, -4, 9, 7]
# mySort(l, key = inverse)
# print(l)




