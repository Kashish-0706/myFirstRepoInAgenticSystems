# defining program to evaluate performance of students

# 1. greeting function
def greeting(name):
    return f"Hello, {name}"

# 2. function to calculate average 
def cal_avg(marks):
    num_subjects = len(marks)
    average = sum(marks)/num_subjects
    return num_subjects, average

# 3. function to evaluate pass/fail
def result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"
    
# 4. main function to call above functions
def main():
    student_name = greeting("Alice")
    total_subjects, avg_score = cal_avg([70, 60, 65])
    final_result = result(avg_score)

    print(student_name)
    print(f"Subjects: {total_subjects}")
    print(f"Average Score: {avg_score}")
    print(f"Result: {final_result}")

main()
 