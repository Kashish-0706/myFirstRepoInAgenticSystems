# reading a file using file handling and performing some operations

numbers = []
with open("results.log", "a") as log_file:
    with open("numbers.txt","r") as file:
        log_file.write("File opened successfully\n")
        for line in file:
            cleaned_line = line.strip()
            if cleaned_line:
                numbers.append(int(cleaned_line))
        log_file.write("Data loaded\n")
    

    total_numbers = len(numbers)
    sum_of_nums = sum(numbers)
    average = sum_of_nums / total_numbers
    log_file.write("Computation completed\n")
    
    log_file.write(f"numbers:{numbers}\n")
    log_file.write(f"Total numbers: {total_numbers}\n")
    log_file.write(f"Sum of numbers: {sum_of_nums}\n")
    log_file.write(f"Average of numbers: {average}\n")
    log_file.write(f"Processing completed\n")