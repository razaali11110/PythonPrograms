4
# Python program to print calendar for given year

# importing calendar library
import calendar


def printcalendar(year):
    # printing calendar
    print(calendar.calendar(year))


# driver program to test above function
year=20202
printcalendar(year)