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

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 12]

print("({}{}{}) {}{}{}-{}{}{}{}".format(*n))
