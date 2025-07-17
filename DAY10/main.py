# main.py
# (This file should be at the same level as the 'OOPModel' directory)

# from OOPModel.employee import Manager(20), Developer(10), Intern(0)
# The line above in your prompt is not standard Python import syntax for instantiating.
# It seems to indicate the intended bonus percentages for each role.
# We'll import the classes directly.

from OOPModel.EmployeeOne import Manager, Developer, Intern

if __name__ == '__main__':
    # Employees
    staff = [
        Manager("Anand", "anand@xyz.com", 90000),
        Developer("Bobby", "bobby@xyz.com", 60000),
        Intern("Chanti", "chanti@xyz.com", 5000)
    ]

    print("--- Employee Bonus Calculation ---")
    for emp in staff:
        print(f"{emp.name} bonus: ${emp.calculateBonus():,.2f}")

    print("\n--- Employee Details ---")
    for emp in staff:
        print(emp) # Uses the __str__ method