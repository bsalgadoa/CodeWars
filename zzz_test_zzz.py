#
#
# lst = [1, 2, 5]
#
# print(lst[-2:])
# print(lst[-2:-1])
# print(lst[-1:])
#
#
# for i in lst[-2:-1]:
#     new_lst_lenght = len(lst) + 3
#     a = 0
#     while a <= new_lst_lenght:
#         lst.append(lst[-1] + lst[-2])
#         a = len(lst) + 1
# print(lst)

#
# def more_than_n (lst, item, n):
#   if lst.count(item) > n:
#     return True
#   return False
#
# #Uncomment the line below when your function is done
#
# print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 0, 6))
#

# n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#
# print("({}{}{}) {}{}{}-{}{}{}{}".format(*n))




# lst1 = [1, 2, 3]
# lst2 = [3, 4, 1]
#
# rev_lst2 = []
# a = -1
# for i in lst2:
#     rev_lst2.append(lst2[a])
#     a = a -1
# print(rev_lst2)
#
# for i in range(len(lst1)):
#     if lst1[i] != rev_lst2[i]:
#         print(False)
#         break
# else: print(True)


#
# def validBraces(string):
#     braces = {"(": ")", "[": "]", "{": "}"}
#     stack = []
#     for character in string:
#         if character in braces.keys():
#             stack.append(character)
#         else:
#             if len(stack) == 0 or braces[stack.pop()] != character:
#                 return False
#     return len(stack) == 0
#
# print(validBraces("[(())]"))


#pares = [10, 20, 30 ,40]
# for i in range(5, 10):
#     print (i)
#     #print (pares[i])
#
# print(list(range(5)))

# pin = 'a234'
# print (type(pin))
# pin = float(pin)
# print (type(pin))
# print(pin.is_integer())
# print(type(pin) == int)
#
# def validate_pin(pin):
#     if len(pin) == 4 or len(pin) == 6:
#         for char in pin:
#             try:
#                 char = int(char)
#             except:
#                 return False
#         return True
#     return False

# from matplotlib import pyplot as plt
#
# import random
#
# numbers_a = range(1,13)
#
# numbers_b = [random.randint(1,1000) for i in numbers_a]
#
# plt.plot(numbers_a,numbers_b)
#
# plt.show()


def solution(a, b):
    return b == a[-1*len(b):]

print(solution('aaa', 'a')) # returns true
#print(solution('abc', 'd')) # returns false
