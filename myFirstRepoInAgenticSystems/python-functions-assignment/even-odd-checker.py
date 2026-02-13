# defining function to check whether the number is even or odd

def check_even_odd(number):
    if number % 2 == 0:
        return "even"  
    else:
        return "odd"
     
# function call
result = check_even_odd(18)
print(f"Number is {result}")