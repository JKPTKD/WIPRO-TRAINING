'''Name: Asima Nayak
    ID:30396
   Email:asimanayak874@gmail.com
   Date:17-July-2025
   Purpose:#You create an object with name and salary
    #print details (name and salary)
    #applyRaise() to the salary
    #print details
    #change the raisePercent using setRaisePercent
    #applyRaise() again
    #print details
 
    #check whether Sunday is working day or not 
'''
import datetime

class Employee:
    raise_percent = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def applyRaise(self):
        self.salary *= self.raise_percent 
        print(f"Applying raise. New salary for {self.name}: ${self.salary:,.2f}") 

    @classmethod
    def setRaisePercent(cls, amount):
        cls.raise_percent = amount
        print(f"Raise percentage updated to: {cls.raise_percent:.2f}")

    @staticmethod
    def isWorkday(day):
        return day.lower() not in ('saturday', 'sunday')


if __name__ == '__main__':
    emp1 = Employee("Alice", 50000)
    print(f"--- Initial Details ---")
    print(f"Employee Name: {emp1.name}")
    print(f"Employee Salary: ${emp1.salary:,.2f}")
    print(f"\n--- After First Raise ---")
    emp1.applyRaise()
    print(f"Employee Name: {emp1.name}")
    print(f"Employee Salary: ${emp1.salary:,.2f}")
    print(f"\n--- Changing Raise Percentage ---")
    Employee.setRaisePercent(1.10) 
    print(f"\n--- After Second Raise with New Percentage ---")
    emp1.applyRaise()
    print(f"Employee Name: {emp1.name}")
    print(f"Employee Salary: ${emp1.salary:,.2f}")
    print(f"\n--- Workday Check ---")
    today = datetime.datetime.now().strftime("%A") 
    print(f"Is today ({today}) a workday? {Employee.isWorkday(today)}")
    print(f"Is Sunday a workday? {Employee.isWorkday('Sunday')}")
    print(f"Is Monday a workday? {Employee.isWorkday('Monday')}")