def valid_braces(string):

    # we need to check if the next brace in the string is ok
    # and also we need to make sure that the last char in string isn't an open brace
    count = 1
    for braces in string:
        if braces == "(":
            if count == len(string) or str(string[count]) in " ]}":
                return False
                break
            else:
                count += 1
        elif braces == "{":
            if count == len(string) or str(string[count]) in " )]":
                return False
                break
            else:
                count += 1
        elif braces == "[":
            if count == len(string) or str(string[count]) in " )}":
                return False
                break
            else:
                count += 1
        else:
            count += 1

    return True

# First i've tried to solve it trough a count sistem but it wasn't enough
# This count aproach only ensures that for every brace open there's a closing

#    count_left_parentheses = 0
#    count_right_parentheses = 0
#    count_left_bracket = 0
#    count_right_brackets = 0
#    count_left_curly = 0
#    count_right_curly = 0
#
#    for braces in string:
#        if braces == "(":
#            count_left_parentheses += -1
#        if braces == ")":
#            count_right_parentheses += 1
#        if braces == "[":
#            count_left_bracket += -1
#        if braces == "]":
#            count_right_brackets += 1
#        if braces == "{":
#            count_left_curly += -1
#        if braces == "}":
#            count_right_curly += 1
#
#    sum_parentheses = count_left_parentheses + count_right_parentheses
#    sum_bracket = count_left_bracket + count_right_brackets
#    sum_curly = count_left_curly + count_right_curly
#
#    if sum_curly or sum_bracket or sum_parentheses != 0:
#        return False
#
#    return True
