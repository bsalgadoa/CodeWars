#-----------------------------------------------------------------
# IGNORE THIS - THIS IS MY PERSONAL TEST FILE THAT I USE DAILY TO QUICKLY TEST DOUBTS
##-----------------------------------------------------------------
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
#     #print (pares[i])e10
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
import random

numbers = list(range(1,51))
stars = list(range(1,13))

random_number1 = random.randint(1,50)
random_number2 = random.randint(1,50)
random_number3 = random.randint(1,50)
random_number4 = random.randint(1,50)
random_number5 = random.randint(1,50)
random_star1 = random.randint(1,12)
random_star2 = random.randint(1,12)

print(random_number1)
print(random_number2)
print(random_number3)
print(random_number4)
print(random_number5)

print(random_star1)
print(random_star2)
if
if (false, ): 
    print ("banana")
else:
    print ("ananas")




#
# def solution(a, b):
#     return b == a[-1*len(b):]
#
# print(solution('aaa', 'a')) # returns true
# #print(solution('abc', 'd')) # returns false


# def diamond(n):
#     if n > 0 and n % 2 == 1:
#         diamond = ""
#         for i in range(n):
#             diamond += " " * abs((n//2) - i)
#             diamond += "*" * (n - abs((n-1) - 2 * i))
#             diamond += "\n"
#         return diamond
#     else:
#         return None
# print(diamond(7))
#
# print((7//2))
