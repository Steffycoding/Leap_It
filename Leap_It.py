def is_leap_year(year):
    """Check if a year is a leap year."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        user_year = int(input("Enter a year: "))
        if is_leap_year(user_year):
            print(f"{user_year} is a leap year!")
        else:
            print(f"{user_year} is not a leap year.")
    except ValueError:
        print("Invalid input. Please enter a valid year.")
