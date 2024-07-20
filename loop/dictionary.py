from tabulate import tabulate

# Creating list of headers
headers = ["stdID", "stdName", "Standard", "Age", "Hindi", "English", "Maths", "Science", "Computer", "Total"]

# Creating list of student records
students = [
    {"stdID": "std101", "stdName": "Ashish", "Standard": "10th", "Age": 15, "Hindi": 67, "English": 89, "Maths": 87, "Science": 89, "Computer": 90, "Total": 422},
    {"stdID": "std102", "stdName": "Abhishek", "Standard": "10th", "Age": 14, "Hindi": 85, "English": 45, "Maths": 48, "Science": 90, "Computer": 45, "Total": 313},
    {"stdID": "std103", "stdName": "Aman", "Standard": "10th", "Age": 15, "Hindi": 23, "English": 56, "Maths": 78, "Science": 78, "Computer": 67, "Total": 302},
    {"stdID": "std104", "stdName": "Rahul", "Standard": "10th", "Age": 14, "Hindi": 45, "English": 67, "Maths": 45, "Science": 46, "Computer": 56, "Total": 258},
    {"stdID": "std105", "stdName": "Ruby", "Standard": "10th", "Age": 13, "Hindi": 89, "English": 67, "Maths": 89, "Science": 93, "Computer": 65, "Total": 403},
    {"stdID": "std106", "stdName": "Sumsn", "Standard": "10th", "Age": 13, "Hindi": 90, "English": 46, "Maths": 67, "Science": 67, "Computer": 67, "Total": 337},
    {"stdID": "std107", "stdName": "Saurabh", "Standard": "10th", "Age": 15, "Hindi": 45, "English": 23, "Maths": 34, "Science": 45, "Computer": 34, "Total": 181},
    {"stdID": "std108", "stdName": "Sunil", "Standard": "10th", "Age": 14, "Hindi": 23, "English": 45, "Maths": 67, "Science": 78, "Computer": 90, "Total": 303},
    {"stdID": "std109", "stdName": "Kamlesh", "Standard": "10th", "Age": 15, "Hindi": 56, "English": 78, "Maths": 90, "Science": 67, "Computer": None, "Total": 345},
    {"stdID": "std110", "stdName": "Rohan", "Standard": "10th", "Age": 15, "Hindi": 34, "English": 12, "Maths": 24, "Science": 45, "Computer": 56, "Total": 171}
]

# Printing the table
print(tabulate(students, headers="keys"))

# Displaying the names of students with English marks greater than 50
students_english_above_50 = [student["stdName"] for student in students if student["English"] > 50]

print("\nStudents with English marks greater than 50:")
for name in students_english_above_50:
    print(name)
    # Task 2: Find and display the names and ages of the students with the top four marks in Math
top_four_math_students = sorted(students, key=lambda x: x["Maths"], reverse=True)[:4]

print("\nStudents with the top four marks in Math:")
for student in top_four_math_students:
    print(f"Name: {student['stdName']}, Age: {student['Age']}")

# Task 3: Display name, ID, and age of students who are bottom three scores in Computer
# Filter out students without Computer marks first
students_with_computer_marks = [student for student in students if student["Computer"] is not None]
bottom_three_computer_students = sorted(students_with_computer_marks, key=lambda x: x["Computer"])[:3]

print("\nStudents with the bottom three scores in Computer:")
for student in bottom_three_computer_students:
    print(f"Name: {student['stdName']}, ID: {student['stdID']}, Age: {student['Age']}")