class Month:
    def __init__(self, month):
        self.month = month

    def get_days(self):
        daysinMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.month < 1 or self.month > 12:
            print("Invalid input. Please enter a number between 1 and 12.")
        else:
            print(f"The number of days in month {self.month} is: {daysinMonth[self.month]}")

try:
    monthNumber = int(input("Enter a number between 1 and 12 to represent a month: "))
    monthDays = Month(monthNumber)
    monthDays.get_days()
except ValueError:
    print("Invalid input. Please enter a valid number.")
