
def monthName(mm):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return months[mm - 1]

def isLeap(yyyy):
    if (yyyy % 4 == 0 and yyyy % 100 != 0) or (yyyy % 400 == 0):
        return True
    else:
        return False


def maxDays(mm, yyyy):
    if mm == 2:
        return 29 if isLeap(yyyy) else 28
    elif mm in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def dayOfWeek(dd, mm, yyyy):
    if mm < 3:
        mm += 12
        yyyy -= 1
    k = yyyy % 100
    j = yyyy // 100
    h = (dd + 13*(mm + 1)//5 + k + k//4 + j//4 + 5*j) % 7
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[h]


def printCalendar(dd, mm, yyyy):
    print("\n", monthName(mm), yyyy)
    print("Sun Mon Tue Wed Thu Fri Sat")

    start_day = dayOfWeek(1, mm, yyyy)
    index = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"].index(start_day)

    for _ in range(index):
        print("    ", end="") 

    for day in range(1, maxDays(mm, yyyy)+1):
        print(f"{day:2}", end="  ")
        index += 1
        if index % 7 == 0:
            print()  
dd = int(input("Enter day: "))
mm = int(input("Enter month: "))
yyyy = int(input("Enter year: "))

print("Day of week:", dayOfWeek(dd, mm, yyyy))
printCalendar(dd, mm, yyyy)
