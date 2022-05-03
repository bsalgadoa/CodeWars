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

string = "(){}[]"

# recive a string
# check if p

count_left_parentheses = 0
count_right_parentheses = 0
count_left_bracket = 0
count_right_brackets = 0
count_left_curly = 0
count_right_curly = 0

for braces in string:
    if braces == "(":
        count_left_parentheses += -1
    if braces == ")":
        count_right_parentheses += 1
    if braces == "[":
        count_left_bracket += -1
    if braces == "]":
        count_right_brackets += 1
    if braces == "{":
        count_left_curly += -1
    if braces == "}":
        count_right_curly += 1



sum_parentheses = count_left_parentheses + count_right_parentheses
sum_bracket = count_left_bracket + count_right_brackets
sum_curly = count_left_curly + count_right_curly

if sum_curly or sum_bracket or sum_parentheses != 0:
    print(False)
else:
    print(True)

print(count_left_parentheses)
print(count_right_parentheses)
print(count_left_bracket)
print(count_right_brackets)
print(count_left_curly)
print(count_right_curly)
