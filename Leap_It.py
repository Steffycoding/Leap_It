from termcolor import colored

def is_leap_year(year):
    """Check if a year is a leap year."""
    # Leap years are divisible by 4 but not by 100, or divisible by 400.
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_february(year):
    """Return the number of days in February for a given year."""
    # February has 29 days in a leap year, otherwise 28 days.
    return 29 if is_leap_year(year) else 28

if __name__ == "__main__":
    try:
        user_year = int(input(colored("Enter a year: ", "yellow")))
        if is_leap_year(user_year):
            print(colored(f"{user_year} is a leap year!", "green"))
        else:
            print(colored(f"{user_year} is not a leap year.", "red"))

        february_days = days_in_february(user_year)
        print(colored(f"Number of days in February {user_year}: {february_days}", "blue"))
    except ValueError:
        print(colored("Invalid input. Please enter a valid year.", "magenta"))
