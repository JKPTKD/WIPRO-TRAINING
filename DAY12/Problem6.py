scores = [85, 30, 65, 40, 25, 90]

# The lambda function as given in the problem
check_pass = lambda marks: "Pass" if marks >= 40 else "Fail"

# Apply the lambda to the list of scores using map()
results = list(map(check_pass, scores))

print(results)