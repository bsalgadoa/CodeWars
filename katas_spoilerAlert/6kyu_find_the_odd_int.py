'''
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
'''


from collections import Counter

def find_it(seq):
    #make a dictonary where the key is the number in the seq and the value is the count of that number in the list
    ocur_dict = dict((i, seq.count(i)) for i in seq)
    # check for the odd value in the dict
    for k, v in ocur_dict.items():
        if v % 2 == 1:
            # return the hey
            return k


print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))


'''
cleaner solution:

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i


'''
