'''Name:Jyotisman Kirti Prakash
   ID:31261
   Email:jyotismankirtiprakash11@gmail.com
   Date:17-July-2025
   Purpose:Class method 
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    @classmethod
    def fromString(cls, data_str):
        name, age = data_str.split(',')
        return cls(name, int(age))
 
    def __str__(self):
        return f'Name: {self.name}   Age: {self.age}'
 
if __name__ == '__main__':
    person1 = Person('Anand', 50)
    person2 = Person.fromString('Bobby, 49')
 
    print(person1)
    print(person2)