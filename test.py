

n = 12345
n = str(n)

(back_string) = n[::-1]
print(back_string)
print(type(back_string))

print(list(back_string))
list2=list(map(int,back_string))
print("List of integers : ",list2)
