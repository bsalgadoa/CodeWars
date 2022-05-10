def solution(number):

## ask user input
## return the sum of all multiples of 3 and 5 < input


# 1st receive the input
# list all the naturals < input
# for each index of the list
    # check if it's multiple 3
    # check if it's multiple 5
    # check if it's multiple of both 3 and 5
        # if so add SUM
# return the sum of all multiples of 3 and 5 < input


    # list all the naturals < input
    list_of_natural = list(range(1,number))

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
    ## if so add it to natural_sum

    # return the sum of all multiples of 3 and 5 < input
    return natural_sum
    pass
