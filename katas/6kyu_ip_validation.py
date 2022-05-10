'''Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.'''

# receive a string
# split that string using .
# convert each i into integer
# check if len of each i is <= 4
# check if each i is >= 0 and <= 255
# split content of each i
# check if first digit is not 0


'''
So.. for an IPv4 to be valid it should consist of 4 octets, with values between 0 and 255.
everything else it's no valid IP
and therefore:
xxx.xxx.xxx.xxx -> max lenght 15
x.x.x.x -> min lenght 7
'''

def is_valid_IP(strng):

    # the string size has to be between 7 and 15
    if len(strng) < 7 or len(strng) > 15:
        return False

    # split that string using .
    splited_ip = strng.split(".")
    # the splited list has to be exactly 4 lenght
    if len(splited_ip) != 4:
         return False

    # check if each i is a digit
    for i in splited_ip:
        if i.isdigit():
            # if it is we have to check if the digit is integer between >= 0 and <= 255
            try:
                i = int(i)
                if i < 0 or i > 255:
                    return False
            except:
                 return False
        else:
            return False

    # we also know that numbers started by 0 are not valid like 001 or 010
    # so we have to exclude any number that starts with 0 wich is not zero.
    for i in range(0,len(splited_ip)):
        if splited_ip[i] !='0':
            if splited_ip[i][0] == "0":
                return False
    return True

strng = ('255.!.111.111')
print(is_valid_IP(strng))
