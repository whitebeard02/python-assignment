def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F (Fail)"

def calculate_total(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total

def calculate_percentage(total, num_subjects):
    percentage = (total / (num_subjects * 100)) * 100
    return percentage

def display_report(name, subjects, marks, total, percentage, grade):
    print("\n========== REPORT CARD ==========")
    print("Student Name:", name)
    print("---------------------------------")
    for i in range(len(subjects)):
        print(subjects[i], ":", marks[i])
    print("---------------------------------")
    print("Total Marks :", total, "/", len(subjects) * 100)
    print("Percentage  :", percentage, "%")
    print("Grade       :", grade)
    print("=================================")


name = input("Enter student name: ")

subjects = ["Maths", "Science", "English", "History", "Computer"]
marks = []

for subject in subjects:
    mark = int(input("Enter marks for " + subject + " (out of 100): "))
    marks.append(mark)

total = calculate_total(marks)
percentage = calculate_percentage(total, len(subjects))
grade = get_grade(percentage)

display_report(name, subjects, marks, total, percentage, grade)