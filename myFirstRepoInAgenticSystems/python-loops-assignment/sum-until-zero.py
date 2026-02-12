# defining code which asks the user for input until user provides zero and finally print sum of all numbers
sum = 0

while True:
    number = int(input("Enter number:" ))
    if number == 0:
        break
    sum = sum + number
print(f"Total sum of numbers is {sum}")
