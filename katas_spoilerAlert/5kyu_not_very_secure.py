'''
In this example you have to validate if a user input string is alphanumeric. The given string is not nil/null/NULL/None, so you don't have to check that.

The string has the following conditions to be alphanumeric:

At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces / underscore
'''


qwe = "PassW0rd"

def alphanumeric(password):
    if password == "":
        return False
    for i in password:
        if i.isdigit() or i.isalpha():
            pass
        else: return False
    return True

print(alphanumeric(qwe))


'''
Now the simpler solution:

def alphanumeric(string):
    return string.isalnum()

just learned about isalnum() wich i didn't knew :)
'''
