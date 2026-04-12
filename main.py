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
        roll=input("Enter Roll number:").strip()
        for s in studentslist:
            if roll == s.roll:
                print("Student Having this roll number already Exists")
                return 
        
        name=input("Enter Your name:")
        degree=input("Enter your Degree:")
        semester=input("Enter your Semester:")
        byear=input("Enter your Birth Year:")
        s=Student(roll,name,degree,semester,byear)
        studentslist.append(s)
        print("Data of student have been inserted.")
        print("-----------------------------------------------------------------------------")
        updatefile()

def displayStudent():#This Displays Student With the help of their roll number.
        seek=input("Enter roll no of Desired Student:")
        found=False
        for s in studentslist:
            if seek ==s.roll:
                found=True
                print("Data is Displayed below\n")
                print(f"ID:{s.roll}\nName:{s.name}\nDate of Birth:{s.byear}\nDegree:{s.degree}\nSemester:{s.semester}\n")
                print("-----------------------------------------------------------------------------")
                break
        if not found:
                print("Student does not Exist")
                print("-------------------------------------------------------------------------------")

def deleteStudent():#This function is used to delete student data from list
        found=False
        seek=input("Enter roll no of Desired Student:")
        for s in studentslist:
            if seek == s.roll:
                found=True
                studentslist.remove(s)
                print("Students Data have been removed Sucessfully.")
                print("-----------------------------------------------------------------------------")
                break
        if found==False:
            print("Student not found!!! ")
            print("---------------------------------------------------------------------------------")
            updatefile()

def updateStudent():#This function is used to update student info with help of roll number
        found=False
        seek=input("Enter roll no of Desired Student:")
        for s in studentslist:
            if s.roll==seek:
                found=True
                s.name=input("Enter name to be updated:")
                s.degree=input("Enter degree to be updated:")
                s.semester=input("Enter semester to be updated:")
                s.byear=input("Enter Date of birth to be updated:")
                print("Students Data updated Sucessfully")
                print("-----------------------------------------------------------------------------")
                break

        if found==False:
            print("Student not found!!!")
            print("----------------------------------------------------------------------------------")
        updatefile()    

def displayAll():#This program is used to display all students data
    print("------------------Data of Student ----------------------------------------")
    if len(studentslist)==0:
        print("No students in list")
        print("--------------------------------------------------")
        return 
    for s in studentslist:
        print(f"ID:{s.roll}\nName:{s.name}\nDate of Birth:{s.byear}\nDegree:{s.degree}\nSemester:{s.semester}\n")
        print("-------------------------------------------------------------------------------------")
        
def updatefile():

    with open('students.txt','w') as f:
        for s in studentslist:
            data=f"{s.roll},{s.name},{s.degree},{s.semester},{s.byear}\n"
            f.write(data)
    
    

def loadFromFile():
    try:
        with open('students.txt','r') as f:
            for line in f:
                data=line.strip().split(',')
                roll=data[0]
                name=data[1]
                degree=data[2]
                semester=data[3]
                byear=data[4]
                s=Student(roll,name,degree,semester,byear)
                studentslist.append(s)
    except:
        pass   

#-------------------------Main Body------------------------------------
loadFromFile()
while(True):
    print("1. Enter a Student")
    print("2. Display Students Info")
    print("3. Update Student Info")
    print("4. Delete Student Info") 
    print("5. Display All Students") 
    print("6. Terminate Program")
    print("--------------------------------------------------------------------------")

    choice=int(input("Enter Your Choice:"))

    if choice==1:
        addStudent()
    elif choice==2:
        displayStudent()
    elif choice == 3:
        updateStudent()
    elif choice == 4:
        deleteStudent()
    elif choice == 5:
        displayAll()
    elif choice==6:
        print("Terminating the Program.")
        break
