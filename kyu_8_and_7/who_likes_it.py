'''
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

'''

def who_likes_it(string):

    if string == []:
        return "no one likes this"
    if len(string) == 1:
        return ('{} like this'.format(string[0]))
    if len(string) == 2:
        return ('{} and {} like this'.format(string[0], string[1]))
    if len(string) == 3 :
        return ('{}, {} and {} like this'.format(string[0], string[1], string[1]))
    if len(string) > 3:
        return ('{}, {} and {} others like this'.format(string[0], string[1], len(string)-2))


a = []
b = ["Peter"]
c = ["Jacob", "Alex"]
d = ["Max", "John", "Mark"]
e = ["Alex", "Jacob", "Mark", "Max"]

print(who_likes_it(a))
print(who_likes_it(b))
print(who_likes_it(c))
print(who_likes_it(d))
print(who_likes_it(e))




''' as always, a cleaner solution:

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this'
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)

'''
