


def hrdf(s):

    minutes_insec = 60
    hours_insec = 3600
    days_insec = 86400
    year_insec = 31536000

    seconds = 0
    minutes = 0
    hours = 0
    days = 0
    years = 0

    if s == 0:
        return 'now'
    else:
        if s < 60:
            return "{} seconds".format(s)
        if s < 3600:
            module_seconds = int(s % 60)
            minutes = int((s - module_seconds)/60)
            if module_seconds > 1:
                return "{} minutes and {} seconds".format(minutes, module_seconds)
            if module_seconds == 1:
                return "{} minutes and {} second".format(minutes, module_seconds)
            if module_seconds == 0:
                if minutes != 1:
                    return "{} minutes".format(minutes)
                return "{} minute".format(minutes)

        if s < 86400:
            module_min = s % 3600
            hours = int((s - module_min)/3600)
            seconds = int(module_min % 60)
            minutes = int((module_min - seconds)/ 60)


            #return "{} hours, {} minutes and {} seconds".format(hours, minutes, seconds)



        if s < 31536000:

            module_hour = s % 86400
            days =  int((s - module_hour)/86400)
            module_min = module_hour % 3600
            hours = int((module_hour - module_min)/3600)
            seconds = int(module_min % 60)
            minutes = int((module_min - seconds)/ 60)

            #return "{} days, {} hours, {} minutes and {} seconds".format(days, hours, minutes, seconds)

        else:
            module_days = s % 31536000
            years = int((s - module_days)/31536000)
            module_hour = module_days % 86400
            days =  int((module_days - module_hour)/86400)
            module_min = module_hour % 3600
            hours = int((module_hour - module_min)/3600)
            seconds = int(module_min % 60)
            minutes = int((module_min - seconds)/ 60)

            #return "{} years, {} days, {} hours, {} minutes and {} seconds".format(years, days, hours, minutes, seconds)


    # -----






        if years != 0 or years != 1:
            a = "{} years".format(years)
        if days == 0:
            b = ""
        if years == 1:
            a = "1 year"



        if days == 0:
            b = ""
        if days == 1:
            b = "1 day"
        else:
            b = "{} days".format(days)

        if hours == 0:
            c = ""
        if hours == 1:
            c = '1 hour'
        else:
            c = "{} years".format(hours)

        if minutes == 0:
            d = ""
        if minutes == 1:
            d = '1 minute'
        else:
            d = "{} minutes".format(minutes)

        if seconds == 0:
            e = ""
        if seconds == 1:
            e = '1 second'
        else:
            e = "{} seconds".format(seconds)

        #return a, b, c, d, e
    return "{}, {}, {}, {} and {}".format(a, b, c, d, e)


            # if seconds > 1:
            #     return "{} minutes and {} seconds".format(minutes, seconds)
            # if seconds == 1:
            #     return "{} minutes and {} second".format(minutes, seconds)
            # if seconds == 0:
            #     if minutes != 1:
            #         return "{} minutes".format(minutes)
            #     return "{} minute".format(minutes)



xx = 31536063+57
print(hrdf(90000))
