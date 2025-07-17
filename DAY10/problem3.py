'''Name:Jyotisman Kirti Prakash
   ID:31261
   Email:jyotismankirtiprakash11@gmail.com
   Date:17-July-2025
   Purpose:Create a Temperature Class with:
		fromCelsius() and fromFahrenheit() as classmethods
		A staticmethod to convert Celsius to Fahrenheit and vice versa 
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, my name is {self.name} and I am {self.age} years old."

class Student(Person): 
    def __init__(self, name, age, grade):
        
        super().__init__(name, age)
       
        self.grade = grade

    def study(self):
        return f"{self.name} is studying hard to achieve a grade of {self.grade}."

    def introduce(self):
       
        person_intro = super().introduce() 
        return f"{person_intro} I am a student with a grade of {self.grade}."
if __name__ == "__main__":
    person1 = Person("Alice", 30)
    print(person1.introduce())

    print("\n--- Student Class Demonstration ---")
    student1 = Student("Bob", 20, "A")
    print(student1.introduce())
    print(student1.study())
    print(f"\nStudent's name (inherited): {student1.name}")
    print(f"Student's age (inherited): {student1.age}")
    print(f"Student's grade (specific to Student): {student1.grade}")

    print("\n--- Another Student ---")
    student2 = Student("Carol", 22, "B+")
    print(student2.introduce())
    print(student2.study())