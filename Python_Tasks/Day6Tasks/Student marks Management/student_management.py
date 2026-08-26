# 1. Subject names stored in a tuple
SUBJECTS = ("Math", "Science", "English")

# 2. Unique student names in a set, student marks dictionary
unique_students = set()
student_marks = {}


def recursive_sum(marks_list):
    """Recursive function to calculate total marks."""
    if not isinstance(marks_list, list):
        raise TypeError("Marks must be contained in a list.")
    if not marks_list:
        return 0
    if not isinstance(marks_list[0], (int, float)):
        raise TypeError("Marks elements must be numeric.")
    
    return marks_list[0] + recursive_sum(marks_list[1:])


def add_student():
    """Function to add a student with marks."""
    try:
        name = input("Enter student name: ").strip()
        marks = []
        
        for subject in SUBJECTS:
            val = input(f"Enter marks for {subject}: ")
            # Validate numeric conversion
            if not val.replace('.', '', 1).isdigit():
                raise ValueError("Invalid input! Please enter numeric marks.")
            marks.append(float(val) if '.' in val else int(val))
        
        unique_students.add(name)
        student_marks[name] = marks
    except ValueError as e:
        print(e)


def display_students():
    """Function to display all student records."""
    if not student_marks:
        print("No student records found.")
        return
    
    for name, marks in student_marks.items():
        print(f"{name} {marks}")


def calculate_average():
    """Function to calculate total and average marks of a student."""
    try:
        name = input("Enter student name to calculate average: ").strip()
        
        if name not in student_marks:
            raise NameError("Student name not found.")
        
        marks = student_marks[name]
        
        # Calculating total using recursive function
        total = recursive_sum(marks)
        
        if len(marks) == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
            
        avg = total / len(marks)
        
        print(f"Total Marks: {total}")
        print(f"Average Marks: {avg}")

    except NameError as e:
        print(e)
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError\n{e}")
    except TypeError:
        print("TypeError\nMarks data type error.")


def main():
    while True:
        print("1. Add Student")
        print("2. Display Students")
        print("3. Calculate Average")
        print("4. Exit")
        
        choice = input("Enter choice: ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            calculate_average()
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()