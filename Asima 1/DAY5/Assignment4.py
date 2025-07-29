'''Name: Asima Nayak
    ID:30396
   Email:asimanayak874@gmail.com
   Date:11-July-2025
   Purpose:
'''
employee = {
    "name": "Sudhakar",
    "position": "Manager",
    "salary": 75000
}
print("Position:", employee["position"])
employee["salary"] = employee["salary"] + (employee["salary"] * 0.10)
print("Updated Salary:", employee["salary"])
employee["department"] = "Training"
print("Updated Employee Dictionary:", employee)
