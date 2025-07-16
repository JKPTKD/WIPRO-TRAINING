import calendar
from datetime import date

class MyDate:
    def __init__(self, dd, mm, yyyy):
        self.dd = dd
        self.mm = mm
        self.yyyy = yyyy

    def isLeap(self):
        return calendar.isleap(self.yyyy)

    def maxDays(self):
        return calendar.monthrange(self.yyyy, self.mm)[1]

    def monthName(self):
        return calendar.month_name[self.mm]

    def printCal(self, newMonth=0, newYear=0):
        m = newMonth if newMonth else self.mm
        y = newYear if newYear else self.yyyy
        print(calendar.month(y, m))

    def printJulianCal(self, newMonth=0, newYear=0):
        m = newMonth if newMonth else self.mm
        y = newYear if newYear else self.yyyy
        print(calendar.TextCalendar().formatmonth(y, m))

    def julianDay(self):
        d = date(self.yyyy, self.mm, self.dd)
        return d.timetuple().tm_yday
if __name__ == '__main__':
    dd = int(input("Enter day: "))
    mm = int(input("Enter month: "))
    yyyy = int(input("Enter year: "))

    my_date = MyDate(dd, mm, yyyy)

    print(f"\nDate: {dd}-{mm}-{yyyy}")
    print("Leap Year:", my_date.isLeap())
    print("Maximum Days in Month:", my_date.maxDays())
    print("Month Name:", my_date.monthName())
    print("Julian Day:", my_date.julianDay())

    print("\nCalendar:")
    my_date.printCal()

    print("Julian-style Text Calendar:")
    my_date.printJulianCal()
