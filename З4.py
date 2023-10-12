def is_year_leap(year):


    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Правда")
    else:
        print("Ложь")

year = int(input())
is_year_leap(year)