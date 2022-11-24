
def leap_year_tester(year):
    if(year % 100 == 0 and year % 400 == 0):
       return True
    if(year % 4 == 0 and not year % 100 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    print(leap_year_tester(2000))
    print(leap_year_tester(1900))
    print(leap_year_tester(2020))
    print(leap_year_tester(2021))


