# code for providing the access to the user
user_age = int(input("Enter your age:" ))

# the stretch requirement
while True:
    user_id = input("Has id? (True/False):" ).lower()
    if user_id == "true":
        has_id = True
        break
    elif user_id == "false":
        has_id = False
        break
    else:
        print("Invalid input! Please type True/False.")

# final output
if user_age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

         



    