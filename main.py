print("Student Management System")
print("----------------------------------")

# -------------------------------Class Section Starts Here-------------------
class Student:
    def __init__(self,roll,name,degree,semester,byear):
        self.roll=roll
        self.name=name
        self.degree=degree
        self.semester=semester
        self.byear=byear

#Storing unit-----------------

studentslist=[]
#------------------------Functions--------------------------------------
def addStudent():# This Function adds student
        roll=input("Enter Roll number:")
        for s in studentslist:
            if roll in s.roll:
                print("Student Having this roll number already Exists")
                return 
        
        name=input("Enter Your name:")
        degree=input("Enter your Degree:")
        semester=input("Enter your Semester:")
        byear=input("Enter your Birth Year:")
        s=Student(roll,name,degree,semester,byear)
        studentslist.append(s)
        print("Data of student have been inserted.")

def displayStudent():
        seek=input("Enter roll no of Desired Student:")
        for s in studentslist:
            if seek ==s.roll:
                print("Data is Displayed below\n")
                print(f"ID:{s.roll}\nName:{s.name}\nDate of Birth:{s.byear}\nDegree:{s.degree}\nSemester:{s.semester}\n")
                print("-----------------------------------------------------------------------------")
            else:
                print("Student does not exists in database.")
        
def updateStudent():
        pass
def deleteStudent():
        pass




#-------------------------Main Body------------------------------------
while(True):
    print("1. Enter a Student")
    print("2. Display Students Info")
    print("3. Update Student Info")
    print("4. Delete Student Info")  
    print("5. Terminate Program")

    choice=int(input("Enter Your Choice:"))

    if choice==1:
        addStudent()
    elif choice==2:
        displayStudent()
    elif choice == 3:
        pass
        updateStudent()
    elif choice == 4:
        studentslist.deleteStudent()
    elif choice==5:
        print("Terminating the Program.")
        break
