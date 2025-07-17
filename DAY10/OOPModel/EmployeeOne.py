# OOPModel/EmployeeOne.py

from abc import ABC, abstractmethod
from OOPModel.PersonOne import Person # Import Person from the same package

class Employee(Person, ABC): # Inherits from Person and ABC (for abstract class)
    def __init__(self, name, email, salary):
        super().__init__(name, email) # Initialize Person's attributes
        self.salary = salary

    @abstractmethod
    def calculateBonus(self):
        """
        Abstract method to calculate bonus. Must be implemented by subclasses.
        """
        pass

    def __str__(self):
        return f"{super().__str__()}, Salary: ${self.salary:,.2f}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.email}', {self.salary})"


class Manager(Employee):
    def __init__(self, name, email, salary):
        super().__init__(name, email, salary)
        # We can add manager-specific attributes here if needed
        # self.bonus_percentage = 0.20 # As per the example Manager(20)

    def calculateBonus(self):
        # Manager bonus is 20% of salary
        # The prompt implies a static percentage for each role, not per instance
        # If Manager(20) in the prompt meant a 20% rate, then:
        return self.salary * 0.20 # Using a fixed 20% for managers


class Developer(Employee):
    def __init__(self, name, email, salary):
        super().__init__(name, email, salary)
        # self.bonus_percentage = 0.10 # As per the example Developer(10)

    def calculateBonus(self):
        # Developer bonus is 10% of salary
        return self.salary * 0.10 # Using a fixed 10% for developers


class Intern(Employee):
    def __init__(self, name, email, salary):
        super().__init__(name, email, salary)
        # self.bonus_amount = 0 # As per the example Intern(0)

    def calculateBonus(self):
        # Intern bonus is 0 (or a fixed small amount)
        # As per the example Intern(0), let's make it 0.
        return 0