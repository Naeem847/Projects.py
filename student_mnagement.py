# Global Mis_id
students=[]
def student_info():
    global students
    
    # local varaibles
    mis_id=input("please enter your mis_id:\n")
    name=input("enter your name:\n")
    age=int(input("enter your age:\n"))
    marks=int(input("enter your marks:\n"))
    print("your mis_id is:",mis_id)
    print("your name is:",name)
    print("your age is:",age)
    print("your marks is:",marks)
    student={
        "mis_id",mis_id,
        "name",name,
        "age",age,
        "marks",marks
    }
    students.append(student)
    print("student added sucessfully\n")
def show_students():
    if not students:
        print("No student in the database yet!!!")
        return
    print("student database!!!")
    for i,student in enumerate(students,start=1):
        print(f"\nstudent{i:}")
        print("mis_id:",student["mis_id"])
        print("name:",student["name"])
        print("age:",student["age"])
        print("marks:",student["marks"])
while True:
    print("----student management-----")   
    print("1 student_info")
    print("2 show_students")
    print("3 Exit")
    choice=int(input("enter your choice:\n"))
    if choice==1:
      student_info()
    elif choice==2:
      show_students()
    elif choice==3:
        print("exiting the program!!!")
        break
    else:
        print("invalid choice!!!")    



