'''

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

'''


def move_zeros(array):

    array_without_zero = list(filter(lambda i: i != 0, array))

    zeros_array = list(filter(lambda zero: zero == 0, array))

    return array_without_zero + zeros_array




move_zeros([1, 0, 1, 2, 0, 1, 3])
