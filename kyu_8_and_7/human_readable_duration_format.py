


def hrdf(seconds):


    minutes_insec = 60
    hours_insec = 3600
    days_insec = 86400
    year_insec = 31536000
    counter = 0
    if seconds == 0:
        return 'now'
    else:
        mod_year = seconds % year_insec
        years = (seconds - mod_year) /year_insec
        if years != 0: counter +=1

        mod_days = mod_year % days_insec
        days = (mod_year - mod_days) / days_insec
        if days != 0: counter +=1

        mod_hours = mod_days % hours_insec
        hours = (mod_days - mod_hours)/ hours_insec
        if hours != 0: counter +=1

        mod_min = mod_hours % minutes_insec
        minutes = (mod_hours - mod_min) / minutes_insec
        if minutes != 0: counter += 1

        sec = mod_min % 60
        #seconds = (mod_min - module_sec) / 60
        if sec != 0: counter += 1

        years = int(years)
        days = int(days)
        hours = int(hours)
        minutes = int(minutes)
        sec = int(sec)



    print("Counter: ", counter)

    print("Years: ", years)
    print("Days: ", days)
    print("Hours: ", hours)
    print("Minutes: ", minutes)
    print("Seconds: ", sec)


    return "{}, {}, {}, {} and {}".format(years, days, hours, minutes, sec)



print(hrdf(3662))

    # if counter == 1:
    #     return
    #
    # if counter == 2:
    #     return
    #
    # if counter > 2:
    #     return
