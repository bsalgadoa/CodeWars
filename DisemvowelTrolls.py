'''Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel.'''

# Receive a string
def disemvowel(string_):

# Converts the string into a list
    string_list = list(string_.strip(''))

# Define a list of letters to be excluded, in this case, vowels
    vowels_list = ['A','E','I','O','U','a','e','i','o','u']
# Creats a new empty list to store no vowels
    no_vowel_list = []

# Goes index by index to check if it a vowel
    for i in string_list:
# if is not, added to no vowel list
        if i not in vowels_list: no_vowel_list.append(i)
        else: pass

# Converts the list into string
    string_= ''.join([str(letter) for letter in no_vowel_list])

# return the string
    return string_
