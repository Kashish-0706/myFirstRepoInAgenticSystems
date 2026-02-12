# code for checking simple accuracy
user_input = input("Enter a floating-point accuracy value: ")
# stretch requirement
try:
    accuracy = float(user_input)
    print(f"Model accuracy is {accuracy}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")

