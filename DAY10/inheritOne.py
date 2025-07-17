'''Name:Jyotisman Kirti Prakash
   ID:31261
   Email:jyotismankirtiprakash11@gmail.com
   Date:17-July-2025
   Purpose:Inheritance
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    @classmethod
    def toPerson(cls, string):
        name, age = ','.split(string)
        return cls(name, int(age))
 
    def __str__(self):
        return f'Name: {self.name}\t\t Age: {self.age}'
 
class Employee(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
 
    def __str__(self):
        return f'{super().__str__()} \tsalary: {self.grade}'
   
if __name__ == '__main__':
    obj = Employee('Anand', 50, 200000)
 
    print(obj)
 
 