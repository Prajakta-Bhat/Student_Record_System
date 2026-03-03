students = []

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

def add_student():
    roll = int(input("Enter Roll Number: "))

    # Check duplicate roll
    for student in students:
        if student["roll"] == roll:
            print("Roll number already exists!")
            return

    name = input("Enter Name: ")

    marks = []
    for i in range(5):
        mark = int(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 5
    grade = calculate_grade(average)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print("----------------------------")
        print("Name:", student["name"])
        print("Roll:", student["roll"])
        print("Marks:", student["marks"])
        print("Total:", student["total"])
        print("Average:", student["average"])
        print("Grade:", student["grade"])

def search_student():
    roll = int(input("Enter Roll Number to search: "))

    for student in students:
        if student["roll"] == roll:
            print("Student Found!")
            print(student)
            return

    print("Student not found.")

def class_statistics():
    if len(students) == 0:
        print("No students available.")
        return

    total_students = len(students)
    total_class_marks = 0

    highest = students[0]
    lowest = students[0]

    for student in students:
        total_class_marks += student["average"]

        if student["average"] > highest["average"]:
            highest = student

        if student["average"] < lowest["average"]:
            lowest = student

    class_avg = total_class_marks / total_students

    print("Total Students:", total_students)
    print("Class Average:", class_avg)
    print("Highest Scorer:", highest["name"])
    print("Lowest Scorer:", lowest["name"])

def update_marks():
    roll = int(input("Enter Roll Number to update: "))

    for student in students:
        if student["roll"] == roll:
            marks = []
            for i in range(5):
                mark = int(input(f"Enter new marks for subject {i + 1}: "))
                marks.append(mark)

            student["marks"] = marks
            student["total"] = sum(marks)
            student["average"] = student["total"] / 5
            student["grade"] = calculate_grade(student["average"])

            print("Marks updated successfully!")
            return

    print("Student not found.")

while True:
    print("\n--- Student Record Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Class Statistics")
    print("5. Update Marks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        class_statistics()
    elif choice == "5":
        update_marks()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")



