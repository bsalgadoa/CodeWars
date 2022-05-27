
'''
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8

'''

def row_sum_odd_numbers(n):
    return n**3


## i thought we had to read a file so I first built this

# def row_sum_odd_numbers(index):
#
#     file = open("file.txt", "r")
#     ls = []
#     for line in file:
#         ls.append(list(map(int, line.split())))
#
#     return (sum(ls[index-1]))

# or
#
# def row_sum_odd_numbers(index):
#
#     file = open("file.txt", "r")
#     l = file.readlines()
#     return sum(list(map(int, l[index-1].split())))

#print(row_sum_odd_numbers(2))
'''
file.txt

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29


'''
