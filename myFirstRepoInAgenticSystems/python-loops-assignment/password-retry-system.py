# defining code which asks the user for a password until the user provides the correct password
correct_password = "admin123"
entered_password = input("Enter password:" )

while entered_password != correct_password:
    entered_password = input("Enter password:" )

print("Access granted")
