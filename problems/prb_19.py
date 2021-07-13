"""
Counting Sundays

You are given the following information, but you may prefer to do some research for yourself.
    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
from dataclasses import dataclass

MONTHS_WITH_30_DAYS = [4, 6, 9, 11]


@dataclass
class Date:
    day: int
    month: int
    year: int


def is_leap_year(year: int) -> bool:
    if year % 100 == 0:
        return True if year % 400 == 0 else False
    return True if year % 4 == 0 else False


def month_last_day(month: int, year: int) -> int:
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return 30 if month in MONTHS_WITH_30_DAYS else 31


def get_next_date(date: Date) -> Date:
    potential_date = date.day + 7
    last_month_date = month_last_day(date.month, date.year)
    if potential_date < last_month_date:
        return Date(potential_date, date.month, date.year)
    final_date = potential_date - last_month_date
    if date.month == 12:
        return Date(final_date, 1, date.year + 1)
    return Date(final_date, date.month + 1, date.year)


if __name__ == "__main__":
    first_day_is_sunday = 0
    first_sunday = Date(7, 1, 1900)  # 1 Jan 1900 was a Monday.
    last_date = first_sunday
    while last_date.year < 2001:
        next_date = get_next_date(last_date)
        if next_date.day == 1:
            if next_date.year > 1900:
                first_day_is_sunday += 1
                last_date = next_date
            else:
                last_date = next_date
        else:
            last_date = next_date
    print(f"{first_day_is_sunday} Sundays fell on the first of the month during"
          f" the twentieth century (1 Jan 1901 to 31 Dec 2000)")
