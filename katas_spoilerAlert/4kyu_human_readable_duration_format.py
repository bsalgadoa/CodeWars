

# receive a string of int (seconds)
# return a string with combination of years, days, hours, minutes and seconds

# important:
    # singular vs plural
    # if a unit is 0, it won't show up.


def format_duration(seconds):

    # so first thing is to determine how many seconds is a minute, hour, day, and year
    minutes_insec = 60
    hours_insec = 3600 #(60*60)
    days_insec = 86400 #(24*3600)
    year_insec = 31536000 #(365*86400)

    # this is for the answer that we'll return
    # the counter will be needeed to know how many outputs the answer will have
    counter = 0 # -> UPDATE: this is equal to len(list_for_answer) so there's no need to create the counter and ocupy space.
    # the asnwer will be composed of the elements added to the list as we go, so we'll need an empy list
    list_for_answer = []

    # if the input is 0 we we don't need to do anything
    if seconds == 0:
        return 'now'
    # if it's not we have to convert it into the desired string output
    else:
        # first we need to know how many years
        # the number of years is the number of seconds minus the module of seconds from how many seconds there is in a year
        # all divided by how many sec there is in a year.
        mod_year = seconds % year_insec
        years = int((seconds - mod_year) / year_insec)
            # years = (seconds - (seconds % 365*24*60*60))/365*24*60*60
            # if the seconds are < than seconds in a year, the module will be the seconds (n % n+1 = n)
            # and seconds - seconds is 0
            # 0 divided by n is always 0
            # and so, years = 0 meaning this formula works for any seconds value

        # after we do the math we can start building the answer
        # if we don't have any years, we wont add anything to our final answer
        # however if we do, we must add that infomation
        if years != 0:
            # if we have an year information to add, we add 1 to the count and the information (singular or plural) to our list.
            counter +=1
            # bellow we'll add the information for a singular answer
            if years == 1:
                list_for_answer.append('1 year')
            # or for the plural answer
            else:
                list_for_answer.append('{} years'.format(years))

        mod_days = mod_year % days_insec
        days = int((mod_year - mod_days) / days_insec)
        # this is the same that we've done for years.
        # we do the math and
        # if we have days to add, we add 1 to the counter and add the singular or plural information to the list
        # if we dont have anything to add (day == 0), we move forward to calculate the hours and so on.
        if days != 0:
            counter +=1
            if days == 1:
                list_for_answer.append('1 day')
            else:
                list_for_answer.append('{} days'.format(days))

        # now we'll replicate what we've done before for hours, minutes and lastly seconds:
        mod_hours = mod_days % hours_insec
        hours = int((mod_days - mod_hours)/ hours_insec)
        if hours != 0:
            counter +=1
            if hours == 1:
                list_for_answer.append('1 hour')
            else:
                list_for_answer.append('{} hours'.format(hours))

        mod_min = mod_hours % minutes_insec
        minutes = int((mod_hours - mod_min) / minutes_insec)
        if minutes != 0:
            counter +=1
            if minutes == 1:
                list_for_answer.append('1 minute')
            else:
                list_for_answer.append('{} minutes'.format(minutes))

        sec = int(mod_min % 60)
        if sec != 0:
            counter +=1
            if sec == 1:
                list_for_answer.append('1 second')
            else:
                list_for_answer.append('{} seconds'.format(sec))

# now that he know how many years, days, hour, minutes and seconds there is
# and we have that infomation saved in the list_for_answer
# we can format out answer so it will builds itself acording to how many data we have.
# for that, we'll use the counter.
# if the counter is 1, it means, that from all the math above, only one field is not zero.
# if it's 2, it means that we have information for 2 fiels and so on.

    return {
        1: '{}',
        2: '{} and {}',
        3: '{}, {} and {}',
        4: '{}, {}, {} and {}',
        5: '{}, {}, {}, {} and {}',
        }[min(5, len(list_for_answer))].format(*list_for_answer[:5])

# so with the information of how many fields we'll have storing in the counter, our answer we'll be the desired form for the number in the counter -> min(5, counter) -> UPDATE: the counter = len(list_for_answer) so we can remove the counter from our fucntion.
# and the fields will be fullfiled by order that they are in our list of answer -> .format(*list_for_answer[:5])



print(format_duration(91))



'''
THIS ARE THE INSTRUCTIONF FORM CODEWARS KATA: Human readable duration format

Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

t is much easier to understand with an example:

* For seconds = 62, your function should return
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

'''
