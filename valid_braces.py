'''Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
'''


'''!!this is my answer but in the end there's a cleanest way of doing it!!'''

def valid_braces(string):

    # we need to check if the next brace in the string does not invalidate the string.
    # for a valid string, after an open braces you can't have a close that it's different.
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

''' now the cleanst solution i've seen: (not mine)
some say it's not efficient and time consuming'''
# this works by removing the matches.
# if the final string it's empty, the string was a valid braces.
def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''
