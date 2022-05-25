
'''
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
'''

def array_diff(a, b):
    # return a fitered list that checks every element in a add it to a new list if a is not in b
    # we can do it through a filter lambda function
    return list(filter(lambda a: a not in b, a))



    ## damn it this work at the first time. first time. I'll never forget eheh
