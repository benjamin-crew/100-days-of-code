def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(month, leap):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap is True:
        month_days[1] += 1
    return(month_days[month])


year = int(input("Which year do you want to check?: "))
month = (int(input("Which month do you want to check?: ")) - 1)

leap = (is_leap(year))
days = days_in_month(month, leap)

print(days)
