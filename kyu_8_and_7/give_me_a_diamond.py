'''Task
You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.'''


# receive a string with int that represent the number of * -> diamond(n)
    # check if the lenght of the string is >= 0.
    # check if it's odd
    # check if every char is an * -> not necessary

# the total number of * is Tn = Tn-2 + n + n-2 -> ended up not being relevant but anyway..
# also the number of lines will be equal to n -> n = l

def diamond(n):


    if n <= 0 or n%2 == 0:
        return None

    if n == 1:
        return '*\n'

    # the n of the diamond, will also be the number of printed lines that we'll need
    # we'll need the midle line, wich will be the line that'll have only *
    half_n = (n - 1)/2

    # of course we need an empty string that will be building on
    # and that will be printed out in the end with the diamond format
    diamond = ''

    # again the string that we will print will be composed by n lines
    # every line has a padron..
    # every line is composed by x spaces, y * and one \n in the end
    # and the number of spaces, * will change while we build the string to print.
    # therefore we'll need those to build the padrons in each line
    space_str = ' '
    diamond_str = '*'
    break_str = '\n'


    # now we just have to find a sequence and perform it
    # a diamond is as tall as as wide so we'll have n lines
    # the midle line will be only composed by *,  times n
    # the first and last line will always have only one * and n-1 / 2 spaces.
    # the others is just a increasing/decreasing sequence of spaces and *
    # when spaces decrease/increase by 1 the * increase/decrease by 2
    # when the number of added \n to the string is equal to n, we stop
        # or when i = n for i in list(range(n))

    count_break = 0
    count_spaces = int(half_n)
    count_diam = 1
    while count_break < n+1:

        # we first add the first half to the empty string:
        if count_break < half_n:
            diamond += space_str * count_spaces
            count_spaces += -1
            diamond += diamond_str * count_diam
            count_diam += 2
            diamond += break_str
            count_break += 1

        # now that we build the 1st half, we now this line is only composed by *
        if count_break == int(half_n):
            diamond += diamond_str * n
            count_break += 1
            diamond += break_str
            count_break += 1
            count_spaces += 1
            count_diam += -2

        # now the last half
        if count_break > half_n:
            diamond += space_str * count_spaces
            count_spaces += 1
            diamond += diamond_str * count_diam
            count_diam += -2
            diamond += break_str
            count_break += 1

    return diamond

print(diamond(7))


'''
now some clever solution: (not mine)

 def diamond(n):
    if n > 0 and n % 2 == 1:
        diamond = ""
        for i in range(n):
            diamond += " " * abs((n//2) - i)
            diamond += "*" * (n - abs((n-1) - 2 * i))
                ### very clever iteration trough *
            diamond += "\n"
        return diamond
    else:
        return None
print(diamond(7))
'''
