# defining a program to evaluate the scores of the students

scores = [72, 45, 89, 30, 60]

for i in scores:
    if i >= 50:
        print("Pass")
        continue
    print("Fail")