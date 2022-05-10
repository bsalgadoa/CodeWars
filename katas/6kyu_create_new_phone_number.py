
'''
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!
'''

def create_phone_number(n):

    #create split lists acording to the number positions
    first3 = n[:3]
    second3 = n[3:6]
    last4 = n[-4:]

    #create empty strings in order to save the elements of the splited lists
    first3_str = ""
    second3_str = ""
    last4_str = ""

    #convert the elements in splited list into string
    for i in first3:
        first3_str += str(i)
    for i in second3:
        second3_str += str(i)
    for i in last4:
        last4_str += str(i)

    #combine each string above into phone number format
    return "({}) {}-{}".format(first3_str, second3_str, last4_str)


'''
Above is my begginer solution.
Now the freakin clever and awsome solution!!

def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

'''
