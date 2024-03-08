def calculate_average(grades):
    return sum(grades) / len(grades)

def determine_grade(average):
    if average >= 90:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'

def student_management_system():
    num_students = int(input("Enter the number of students: "))
    for i in range(1, num_students + 1):
        student_name = input(f"Enter the name of student {i}: ")
        num_subjects = int(input("Enter the number of subjects: "))
        grades = [float(input(f"Enter the grade for subject (out of 100) {j}: ")) 
        for j in range(1, num_subjects + 1)]

        average_grade = calculate_average(grades)
        grade = determine_grade(average_grade)

        print(f"\nStudent: {student_name}")
        print(f"Average Grade: {average_grade:.2f}")
        print(f"Final Grade: {grade}\n")

student_management_system()
