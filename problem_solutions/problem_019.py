"""
Problem 19 - Counting Sundays
https://projecteuler.net/problem=19
"""


days_in_months = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 30,
                  "Oct": 31, "Nov": 30, "Dec": 31}
days = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"]


def counting_sundays():
    total_sundays = 0
    year = 1901
    day = "Tues"
    while year < 2001:
        sundays, next_yr_day_index = year_data(year, day)
        total_sundays += sundays
        day = days[next_yr_day_index]
        year += 1
    return total_sundays


def year_data(year, day_of_week):
    """
    Helper function that prints out all the days of a year.
    We require the starting day of the week as well so that it's accurate.

    Returns the number of sundays that fell on the first of the month for this year, as well
    as the day index of December 31st, so that we know what day the next year starts.
    """
    first_of_month_sundays = 0
    day_index = days.index(day_of_week)

    # For each month, go through all of the days
    for month in list(days_in_months.keys()):
        # get the number of days in this month
        days_in_month = days_in_months[month]
        if month == "Feb" and is_leap_year(year):
            days_in_month = 29

        # go through the days, and update the day of week after iterating over each day
        for day in range(1, days_in_month + 1):
            # check if this is a sunday on the first day of the month
            if day == 1 and days[day_index] == "Sun":
                first_of_month_sundays += 1

            print(year, month, day, days[day_index])
            day_index = advance_day_index(day_index)

    return (first_of_month_sundays, day_index)


def advance_day_index(index):
    if index == len(days) - 1:
        return 0
    else:
        return index + 1


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


if __name__ == "__main__":
    answer = counting_sundays()
    print(answer)
