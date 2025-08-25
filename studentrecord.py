# Student Management System

# Step 1: Create a Student class
class Student:
    def __init__(self, name, age, grade):
        self.name = name      # String (data type)
        self.age = age        # Integer (data type)
        self.grade = grade    # String (data type)

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


# Step 2: Use a list to store students
students = []   # Empty list (data structure)

# Step 3: Menu for user interaction
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        # Input student details (variables)
        name = input("Enter name: ")
        age = int(input("Enter age: "))   # Convert input to integer
        grade = input("Enter grade: ")

        # Create a Student object and store it
        student = Student(name, age, grade)
        students.append(student)
        print(f"✅ Student {name} added successfully!")

    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            print("\n--- Student List ---")
            for s in students:
                print(s.get_details())

    elif choice == "3":
        print("Exiting program... 👋")
        break

    else:
        print("Invalid choice! Try again.")
