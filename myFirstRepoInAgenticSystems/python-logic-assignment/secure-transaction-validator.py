# defining the code for secure transaction
account_balance =int(input("Enter your account balance:" ))
withdrawal_amount = int(input("Enter the amount to be withdrawn:" ))

# stretch requirement
while True:
    verification_status = input("Enter your verification status(True/False):" ).lower()
    if verification_status == "true":
        verified = True
        break
    elif verification_status == "false":
        verified = False
        break
    else:
        print("Invalid input! Please enter True/False.")

# final process
if withdrawal_amount <= account_balance and verified:
    print("Withdrawal successful") 
else:
    print("Transaction denied")
