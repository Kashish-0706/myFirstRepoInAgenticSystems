# defining a program to check the role of employee using tuples and sets

# details of employee stored in form of set
details = (121, "Julian Rhodes", "Cybersecurity")

# roles of employee stored in form of set
roles = {"admin", "viewer", "editor"}

# print all details of employee
print("Employee ID:", details[0])
print("Employee Name:", details[1])
print("Department:", details[2])

# check admi access of employee
if "admin" in roles:
    print("Admin Access: Yes")
else:
    print("Admin Access: No")