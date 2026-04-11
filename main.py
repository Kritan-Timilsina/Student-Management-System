print("Student Management System")
print("----------------------------------")
class Student:
    def __init__(self,roll,name,Degree,Semester,dob):
        self.roll=roll
        self.name=name
        self.Degree=Degree
        self.Semester=Semester
        self.dob=dob

    def displayStudent(self):
        print(f"ID:{self.roll}\nName:{self.name}\nDate of Birth:{self.dob}\nDegree:{self.Degree}\nSemester:{self.Semester}\n")
    def updateStudent():
        pass
    def deleteStudent():
        pass


while(True):
    print("1. Enter a Student.\n")
    print("2. Display Students Info.")
    print("3. Update Student Info")
    print("4. Delete Student Info")   


#Storing unit-----------------
students=[]


    choice=int(input("Enter Your Choice:"))

    if choice==1:
        addStudent()
    elif choice==2:
        displayStudent()
    elif choice == 3:
        updateStudent()
    elif choice == 4:
        deleteStudent()
    elif choice==5:
        print("Terminating the Program.")
        break
