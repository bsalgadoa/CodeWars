
'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.
'''

# ask user input
# return the sum of all multiples of 3 and 5 < input


# ask user input
    # make sure is natural -> int > 0
    # save input
# list all the naturals < input
# for each index of the list
    # check if it's multiple 3
    # check if it's multiple 5
    # check if it's multiple of both 3 and 5
        # if so add SUM
# return the sum of all multiples of 3 and 5 < input

## ask user input
# return the sum of all multiples of 3 and 5 < input
print('\n')
print('This program sums the natural numbers that are multiple of 3 or 5, below your given input.  ')
# ask user input and save it
user_input = input('Therefore, please provide us your natural number: ')

# make sure is natural -> int > 0
while user_input != "":
    try:
        user_input = int(user_input)
        if user_input > 0:
            break
        elif user_input == 0:
            print('Sorry, Zero is not a natural number. ')
            user_input = input('Please provide us your natural number: ')
        else:
            print('Nice try. Natural numbers are greater than 0. ')
            user_input = input('Please provide us your natural number: ')
    except:
        pass
        print('\nIncorrect input.')
        user_input = input('Please insert your natural number: ')

# list all the naturals < input
list_of_natural = list(range(1,user_input))

# define a sum variable to store the values
natural_sum = 0
# for each index of the list
for natural in list_of_natural:
#     # check if it's multiple of3
    if (natural%3)==0:
        natural_sum += natural
#     # check if it's multiple of 5
    elif (natural%5)==0:
        natural_sum += natural
        ## the way this if andn elif are built automaticly exclude the double count scenario.
## if so add it to sum variable

# return the sum of all multiples of 3 and 5 < input
print('The sum of multiple numbers of 3 or 5 below your input is: ', natural_sum)
