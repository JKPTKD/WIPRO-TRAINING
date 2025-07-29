'''Name: Asima Nayak
    ID:30396
   Email:asimanayak874@gmail.com
   Date:11-July-2025
   Purpose: Given a list of tuples (course,student),group students by course.
   data=[("Math", "Bobby"),("Science", "Bablu"),("Math", "Pinkie"),("Math", "Ram"),("Science", "Chintu")]
'''
# Input data
data = [
    ("Math", "Bobby"),
    ("Science", "Bablu"),
    ("Math", "Pinkie"),
    ("Math", "Ram"),
    ("Science", "Chintu")
]


course_groups = {}

for course, student in data:
    if course not in course_groups:
        course_groups[course] = set()  
    course_groups[course].add(student)


print(course_groups)
