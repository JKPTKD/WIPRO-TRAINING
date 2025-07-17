'''Name:Jyotisman Kirti Prakash
   ID:31261
   Email:jyotismankirtiprakash11@gmail.com
   Date:17-July-2025
   Purpose:Create a Student class with:
		An alternative constructor that accepts name|age|grade in a string.		
		A static method to check if a grade is a pass (>= 50). 
'''
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    @classmethod
    def from_string(cls, student_info_string):
        """
        Alternative constructor to create a Student object from a string
        in the format 'name|age|grade'.
        """
        parts = student_info_string.split('|')
        if len(parts) == 3:
            name = parts[0].strip()
            try:
                age = int(parts[1].strip())
                grade = int(parts[2].strip())
                return cls(name, age, grade)
            except ValueError:
                print("Error: Age and grade must be integers. Could not create Student object.")
                return None
        else:
            print("Error: Invalid string format. Expected 'name|age|grade'. Could not create Student object.")
            return None

    @staticmethod
    def is_pass(grade):
        """
        Static method to check if a grade is a pass (>= 50).
        """
        return grade >= 50

    def __str__(self):
        """
        Returns a string representation of the Student object.
        """
        return f"Student Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

# --- Demonstration ---
if __name__ == "__main__":
    print("--- Student Class Demonstration ---")

    # 1. Creating a Student object using the regular constructor
    student1 = Student("Alice Smith", 20, 78)
    print(f"Student 1 (regular constructor): {student1}")
    print(f"Is {student1.name}'s grade a pass? {Student.is_pass(student1.grade)}")

    print("\n--- Using Alternative Constructor (from_string) ---")

    # 2. Creating a Student object using the alternative constructor (valid string)
    student_info_str_1 = "Bob Johnson|22|45"
    student2 = Student.from_string(student_info_str_1)
    if student2:
        print(f"Student 2 (from_string): {student2}")
        print(f"Is {student2.name}'s grade a pass? {Student.is_pass(student2.grade)}")
    else:
        print(f"Failed to create student from string: '{student_info_str_1}'")


    student_info_str_2 = "Charlie Brown|19|92"
    student3 = Student.from_string(student_info_str_2)
    if student3:
        print(f"Student 3 (from_string): {student3}")
        print(f"Is {student3.name}'s grade a pass? {Student.is_pass(student3.grade)}")
    else:
        print(f"Failed to create student from string: '{student_info_str_2}'")

    print("\n--- Testing Edge Cases for from_string ---")

    # 3. Testing with invalid string format (missing part)
    student_invalid_format = "David Lee|21"
    student4 = Student.from_string(student_invalid_format) # This will print an error message

    # 4. Testing with invalid data type for age/grade
    student_invalid_data = "Eve Davis|twenty|80"
    student5 = Student.from_string(student_invalid_data) # This will print an error message

    print("\n--- Testing Static Method Directly ---")
    print(f"Is grade 65 a pass? {Student.is_pass(65)}")
    print(f"Is grade 49 a pass? {Student.is_pass(49)}")
    print(f"Is grade 50 a pass? {Student.is_pass(50)}")