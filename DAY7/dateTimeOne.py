from datetime import datetime, timedelta

now = datetime.now()
print(f'time: {now.strftime("%H:%M:%S")}')
print(f'Date: {now.strftime("%d-%m-%Y")}')
print(f'Date: {now.strftime("%d-%B-%Y")}')
print(f'Date: {now.strftime("%d-%b-%Y")}')
print(f'Date: {now.strftime("%d-%B-%y")}')
print(f'Date: {now.strftime("%d-%b-%y")}')
print(f'today is : {now.strftime("%a")}')
print(f'today is : {now.strftime("%A")}')

yesterday = now - timedelta(days=3)
print(yesterday.date())

doj = datetime(2008, 12, 1)
noDays = (now - doj).days
print(f'Years: {noDays // 365}  Months: {noDays // 12}')
