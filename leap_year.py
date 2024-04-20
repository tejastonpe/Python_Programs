def leap_year(year):
    if (year%4 == 0 and year % 100 !=0) or (year % 400 ==0):
        print(f"{year} is leap year")
    else:
        print(f"{year} is not a leap year")


if __name__=="__main__":
    try:
        year=int(input("Enter year: "))
        if len(str(year))< 4:
            raise ValueError("Enter valid year with 4-digits")
        leap_year(year)
    except ValueError as e:
        print(e)