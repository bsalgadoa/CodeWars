
'''
First aproach was to check if the square root of the given number n was an int or a float.
If it was a inte, it was a perfect square.
However, the square root always return the answer as a float type and therefore it can't be.
So the nesxt aproach was to check if the float and ceiling of the square root was the same. this is true only if the number is an integer. for any float number this wont be true and based on that the solution was built
'''

'''
note 2:
After searching for a better method I discovered the is_integer() function and so a better solution would be:

def is_square(n):
    return n>=0 and (n**0,5).is_integer()

clean and beautifull
'''


# receive an integer
def is_square(n):

    import math

    if n<0:
        perfect_square = False

    else:
        n_root = n**0.5
        if math.floor(n_root) == math.ceil(n_root):
            perfect_square = True
        else:
            perfect_square = False

    return perfect_square
