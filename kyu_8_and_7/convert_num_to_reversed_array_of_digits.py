'''Given a random non-negative number, you have to return the digits of this number within an array in reverse order.'''

#receive an int
def digitize(n):
    # convert it into string
    n = str(n)
    # invert string
    back_string = n[::-1]
    # convert the type of elements from str to int and return it
    return list(map(int,back_string))


#receive an int
#def digitize(n):
    # convert it into string
#    n = str(n)
    # invert string
#    back_string = n[::-1]
    # convert the back_string into list
#    list_back_string = list(back_string)
    # convert the type of elements from str to int
#    int_list_back_string = list(map(int,list_back_string))
    # return it
#    return int_list_back_string
