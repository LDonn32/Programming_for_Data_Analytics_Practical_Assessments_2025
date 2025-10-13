# assignment02-bankholidays.py
# Author: Laura Donnelly

# Write a program that prints out the bank holidays in Northern Ireland for the year 2025.



# Define a function that returns a list of tuples containing the date and name of each bank holiday in Northern Ireland for 2025.
def ni_bank_holidays_2025():
    
    return [
        ("2025-01-01", "New Year’s Day"),
        ("2025-03-17", "St Patrick’s Day"),
        ("2025-04-18", "Good Friday"),
        ("2025-04-21", "Easter Monday"),
        ("2025-05-05", "Early May Bank Holiday"),
        ("2025-05-26", "Spring Bank Holiday"),
        ("2025-07-14", "Battle of the Boyne / Orangemen’s Day (substitute)"),
        ("2025-08-25", "Summer Bank Holiday"),
        ("2025-12-25", "Christmas Day"),
        ("2025-12-26", "Boxing Day"),
    ]
# Main program
def main():
    holidays = ni_bank_holidays_2025()
    # Print the dates.
    print("Northern Ireland Bank Holidays in 2025:")
    # Use a for loop to print each holiday on a new line.
    for date_str, name in holidays:
        print(f"  {date_str} — {name}")

# Directly call main() so the program runs automatically
main()











