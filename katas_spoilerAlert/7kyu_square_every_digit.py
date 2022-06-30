'''Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer'''


def square_digits(num):
    str_num = str(num)
    sq_digts = str()
    for i in str_num:
        a = int(i)
        sq_digts += str(a**2)
    return int(sq_digts)

if __name__ == '__main__':
    import timeit as t
    #print(t.timeit(solution, number=2_0000))
    #solution()
    print("solution:", square_digits(9119))


'''
cleaner code:

def square_digits(num):
    sq_digts = str()
    for i in str(num):
        sq_digts += str(int(x)**2)
    return int(sq_digts)

'''
