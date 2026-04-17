print("Student Management System")
print("----------------------------------")

# -------------------------------Class Section Starts Here-------------------


class Student:
    def __init__(self, roll, name, gender, degree, semester, byear):
        self.roll = roll
        self.name = name
        self.gender = gender
        self.degree = degree
        self.semester = semester
        self.byear = byear

# Storing unit-----------------


studentslist = []
# ------------------------Functions--------------------------------------


def addStudent():  # This Function adds student
    try:
        roll = int(input("Enter Roll number:"))
    except:
        print("Please enter valid input.")
        return

    for s in studentslist:
        if roll == s.roll:
            print("Student Having this roll number already Exists")
            print(
                "-----------------------------------------------------------------------------")
            return

    try:
        name = str(input("Enter your name:"))
        gender = str(input("Enter your Gender:"))
        degree = str(input("Enter your Degree:"))
        semester = str(input("Enter your Semester:"))
        byear = str(input("Enter your Birth Year:"))
    except:
        print("Please enter valid input.")
        return
    s = Student(roll, name, gender, degree, semester, byear)
    studentslist.append(s)
    print("Data of student have been inserted.")
    print("-----------------------------------------------------------------------------")
    updatefile()


def displayStudent():  # This Displays Student With the help of their roll number.
    try:
        seek = int(input("Enter roll no of Desired Student:"))
    except:
        print("Please enter valid input.")
        return

    found = False
    for s in studentslist:
        if seek == s.roll:
            found = True
            print("Data is Displayed below\n")
            print(
                f"ID:{s.roll}\nName:{s.name}\nGender:{s.gender}\nDate of Birth:{s.byear}\nDegree:{s.degree}\nSemester:{s.semester}\n")
            print(
                "-----------------------------------------------------------------------------")
            break
    if not found:
        print("Student does not Exist")
        print("-------------------------------------------------------------------------------")


def deleteStudent():  # This function is used to delete student data from list
    found = False
    try:
        seek = int(input("Enter roll no of Desired Student:"))
    except:
        print("Please enter valid input")
        return
    for s in studentslist:
        if seek == s.roll:
            found = True
            studentslist.remove(s)
            print("Students Data have been removed Sucessfully.")
            updatefile()
            print(
                "-----------------------------------------------------------------------------")
            break
    if found == False:
        print("Student not found!!! ")
        print("---------------------------------------------------------------------------------")


def updateStudent():  # This function is used to update student info with help of roll number
    found = False
    try:
        seek = int(input("Enter roll no of Desired Student:"))
    except:
        print("Please enter valid input.")
        return
    for s in studentslist:
        if s.roll == seek:
            found = True
            try:
                s.name = input("Enter name to be updated:").strip()
                s.degree = input("Enter degree to be updated:").strip()
                s.gender = input("Enter gender to be upgraded:").strip()
                s.semester = input("Enter semester to be updated:").strip()
                s.byear = input("Enter Date of birth to be updated:")
                print("Students Data updated Sucessfully")
                updatefile()
                print(
                    "---------------------------------------------------------------------------")
                break
            except:
                print("Please enter valid input.")
                return
            print(
                "-----------------------------------------------------------------------------")
    if found == False:
        print("Student not found!!!")
        print("----------------------------------------------------------------------------------")


def displayAll():  # This program is used to display all students data
    print("------------------Data of Student ----------------------------------------")
    if len(studentslist) == 0:
        print("No students in list")
        print("--------------------------------------------------")
        return
    for s in studentslist:
        print(f"ID:{s.roll}\nName:{s.name}\nGender:{s.gender}Date of Birth:{s.byear}\nDegree:{s.degree}\nSemester:{s.semester}\n")
        print("-------------------------------------------------------------------------------------")


def updatefile():

    with open('students.txt', 'w') as f:
        for s in studentslist:
            data = f"{s.roll},{s.name},{s.gender},{s.degree},{s.semester},{s.byear}\n"
            f.write(data)


def loadFromFile():
    studentslist.clear()
    try:
        with open('students.txt', 'r') as f:
            for line in f:

                data = line.strip().split(',')
                if len(data) != 6:
                    continue
                roll = int(data[0])
                name = data[1]
                gender = data[2]
                degree = data[3]
                semester = data[4]
                byear = data[5]
                s = Student(roll, name, gender, degree, semester, byear)
                studentslist.append(s)
    except FileNotFoundError:
        print("Loading of file failed")
        return

# -------------------------Main Body------------------------------------


loadFromFile()
while (True):
    print("1. Enter a Student")
    print("2. Display Students Info")
    print("3. Update Student Info")
    print("4. Delete Student Info")
    print("5. Display All Students")
    print("6. Terminate Program")
    print("--------------------------------------------------------------------------")
    try:
        choice = int(input("Enter Your Choice:"))
    except:
        print("Please enter valid input.")
        continue

    if choice == 1:
        addStudent()
    elif choice == 2:
        displayStudent()
    elif choice == 3:
        updateStudent()
    elif choice == 4:
        deleteStudent()
    elif choice == 5:
        displayAll()
    elif choice == 6:
        print("Terminating the Program.")
        break
