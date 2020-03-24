##################################################
# APS106 Winter 2020 - Lab 4 - Holiday Countdown #
##################################################


def next_holiday(year, month, day):
    """
    (int, int, int) -> [str, int]
    A function that is passed a year, month, and day and then determines:
      1. the name of the next Ontario statuatory holiday
      2. the number of days until that holiday
    The function returns the name and 
    number of days as a two element list.
    
    >>> next_holiday(2020,4,31)
    ['invalid day',-1]
    
    >>> next_holiday(2004,12,4)
    ['christmas day', 21]


    >>> next_holiday(2019,6,30)
    ['canada day', 1] 
    """
    
    ## TODO: YOUR CODE HERE

    # Check for leap year
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap_year = True
    else:
        leap_year = False

    # Find the next holiday
    if month == 1:
        days_in_month = 31
        if day > days_in_month or day < 0:
            return ['invalid day', -1]
        else:
            holiday = "family day"
            days_until = (days_in_month - day) + 17
            return [holiday, days_until]

    elif month == 2:
        if leap_year:
            days_in_month = 29
        else:
            days_in_month = 28

        if day > days_in_month or day < 0:
            return ['invalid day', -1]
        else:
            holiday = "good friday"
            days_until = (days_in_month - day) + 31 + 10
            return [holiday, days_until]

    elif month == 3:
        days_in_month = 31

        if day > days_in_month or day < 0:
            return ['invalid day', -1]
        else:
            holiday = "good friday"
            days_until = (days_in_month - day) + 10
            return [holiday, days_until]

    elif month == 4:
        days_in_month = 30

        if day > days_in_month or day < 0:
            return ['invalid day', -1]
        else:
            if day < 10:
                holiday = "good friday"
                days_until = 10 - day
                return [holiday, days_until]
            else:
                holiday = "victoria day"
                days_until = (days_in_month - day) + 18
                return [holiday, days_until]

    elif month == 5:
        days_in_month = 31

        if day > days_in_month or day < 0:
            return ['invalid day', -1]
        else:
            if day < 18:
                holiday = "victoria day"
                days_until = 18 - day
                return [holiday, days_until]
            else:
                holiday = "canada day"
                days_until = (days_in_month - day) + 30 + 1
                return [holiday, days_until]

    elif month == 6:
        days_in_month = 30

        if day > days_in_month or day < 0:
            return ['invalid day', -1]
        else:
            holiday = "canada day"
            days_until = (days_in_month - day) + 1
            return [holiday, days_until]

    elif month == 7:
        days_in_month = 31

        if day > days_in_month or day < 0:
            return ['invalid day', -1]
        else:
            holiday = "civic holiday"
            days_until = (days_in_month - day) + 3
            return [holiday, days_until]

    elif month == 8:
        days_in_month = 31

        if day > days_in_month or day < 0:
            return ['invalid day', -1]
        else:
            if day < 3:
                holiday = "civic holiday"
                days_until = 3 - day
                return [holiday, days_until]
            else:
                holiday = "labour day"
                days_until = (days_in_month - day) + 7
                return [holiday, days_until]

    elif month == 9:
        days_in_month = 30

        if day > days_in_month or day < 0:
            return ['invalid day', -1]
        else:
            if day < 7:
                holiday = "labour day"
                days_until = 7 - day
                return [holiday, days_until]
            else:
                holiday = "thanksgiving day"
                days_until = (days_in_month - day) + 12
                return [holiday, days_until]

    elif month == 10:
        days_in_month = 31

        if day > days_in_month or day < 0:
            return ['invalid day', -1]
        else:
            if day < 12:
                holiday = "thanksgiving day"
                days_until = 12 - day
                return [holiday, days_until]
            else:
                holiday = "christmas day"
                days_until = (days_in_month - day) + 30 + 25
                return [holiday, days_until]

    elif month == 11:
        days_in_month = 30

        if day > days_in_month or day < 0:
            return ['invalid day', -1]
        else:
            holiday = "christmas day"
            days_until = (days_in_month - day) + 25
            return [holiday, days_until]

    elif month == 12:
        days_in_month = 31

        if day > days_in_month or day < 0:
            return ['invalid day', -1]
        else:
            if day < 25:
                holiday = "christmas day"
                days_until = 25 - day
                return [holiday, days_until]

            elif day == 25:
                holiday = "boxing day"
                days_until = 26 - day
                return [holiday, days_until]

            else:
                holiday = "new year's day"
                days_until = (days_in_month - day) + 1
                return [holiday, days_until]

    else:
        return ['invalid month', -1]
