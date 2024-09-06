def leap_year_checker(year_number):
    year_number = int(year_number)
    if year_number % 4 == 0:
        if year_number % 100 == 0 and year_number % 400 == 0:
            print(f'{year_number} - leap year')
        elif year_number % 100 == 0 and year_number % 400 != 0:
            print(f'{year_number} - not a leap year')
        else:
            print(f'{year_number} - leap year')
    else:
        print(f'{year_number} - not a leap year')

leap_year_checker(1712)
leap_year_checker(1913)