# defining a program to evaluate marks of students
marks = [78, 85, 90, 65, 72, 88, 92, 80]

highest = max(marks)
lowest = min(marks)
average = sum(marks)/len(marks)

print(f"Full list: {marks}")
print(f"First 3 marks: {marks[0:3]}")
print(f"Last 3 marks{marks[5:8]}")
print(f"Highest marks: {highest}")
print(f"Lowest marks: {lowest}")
print(f"Average marks: {average}")
