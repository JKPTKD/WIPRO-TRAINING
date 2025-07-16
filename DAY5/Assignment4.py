'''Name:Jyotisman Kirti Prakash
   ID:31261
   Email:jyotismankirtiprakash11@gmail.com
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
