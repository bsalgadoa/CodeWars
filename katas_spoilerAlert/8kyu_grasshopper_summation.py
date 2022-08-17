'''
Summation
Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

For example:

summation(2) -> 3
1 + 2

summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8
'''

## just remind the Gauss formula to find the sum of a sequence of n natural numbers.

def summation(num):
    return (num * (num+1)) / 2
