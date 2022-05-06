'''Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

Write a function that will take the number of petals of each flower and return True if they are in love and false if they aren't.'''


##My solution

def lovefunc( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 != 0:
        return True
    if flower2 % 2 == 0 and flower1 % 2 != 0:
        return True
    else:
        return False


## simpler solution
## to be true one of them as to be odd and the other even.
## the sum of an odd with an even is always odd
## so if it's module is 1 - true

def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2

print(lovefunc( 1, 2 )%2)

#note: For numerical types like integers and floating-points, zero values are false and non-zero values are true
