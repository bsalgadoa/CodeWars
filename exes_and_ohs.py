# receive string
def xo(s):

# convert list string into list
    s_list = list(s.strip(''))

    o_count = 0
    x_count = 0
# check all the elements in the string for o and x:
    for i in s_list:
    # if it's "o" add it to o_ count
        if i == "o" or i == "O":
            o_count += 1
    # if it's "x" add it to x_count
        elif i == "x" or i == "X":
            x_count += 1
        else:
            pass
# return the comparisson:
    return x_count == o_count
