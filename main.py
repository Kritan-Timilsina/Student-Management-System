print("Student Management System")
print("-"*70)

# -------------------------------Class Section Starts Here-------------------
from db import get_connection

class Student:
    def __init__(self, roll, name, gender, degree, semester, byear):
        self.roll = roll
        self.name = name
        self.gender = gender
        self.degree = degree
        self.semester = semester
        self.byear = byear




studentslist = []
# ------------------------Functions--------------------------------------
def create_table(): # create table if it doesnot exist 
    conn=get_connection()
    cur=conn.cursor()
    try:
        cur.execute("""CREATE TABLE IF NOT EXISTS students(
            roll int primary key,
            name varchar (50),
            gender varchar (10),
            degree varchar(20),
            semester int,
            byear int not null );""")
        print("Table Created Sucessfully!!!")

        conn.commit()
    except Exception as e:
        print("Error",e)
    finally:
        cur.close()
        conn.close()
    


def addStudent():  # This Function adds student
    try:
        roll = int(input("Enter Roll number:"))
    except:
        print("Please enter valid input.")
        return
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("""
        select 1 from students where roll =%s
        """,(roll,))
    exist=cur.fetchone()
    if exist:
        print("This Student Already Exists in database")
        cur.close()
        conn.close()
        return 


    try:
        name = str(input("Enter your name:"))
        gender = str(input("Enter your Gender:"))
        degree = str(input("Enter your Degree:"))
        semester = int(input("Enter your Semester:"))
        byear = int(input("Enter your Birth Year:"))
    except:
        print("Please enter valid input.")
        print("-"*70)
        return
    try:
        cur.execute("""
        Insert into students(roll,name,gender,degree,semester,byear)
                    values(%s,%s,%s,%s,%s,%s)""",(roll,name,gender,degree,semester,byear))
        conn.commit()
        print("Data of student have been inserted.")
        print("-"*70)
    except Exception as e :
        print("Error:",e)
    finally:  
        cur.close()
        conn.close()
    
    
    print("-"*70)
    


def displayStudent():  # This Displays Student With the help of their roll number.
    cur=None
    conn=None 

    
    try:
        conn=get_connection()
        cur=conn.cursor()
        roll = int(input("Enter roll no of Desired Student:"))
        cur.execute("""Select * from students where roll =%s""",(roll,))
        student=cur.fetchone()
        if not student:
            print("Student with this roll doesnot exists")
            return 
        
        print(f"Roll:{student[0]}\nName:{student[1]}\nGender:{student[2]}\nDegree:{student[3]}\nSemester:{student[4]}\nBirth Year:{student[5]}\n")
        print("-"*70)
    except:
        print("Please enter valid input.")
        print("-"*70)
        return
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
    


def deleteStudent():  # This function is used to delete student data from database
    conn=None
    cur=None
    try:
        roll=int(input("Enter roll number of student:"))
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("select * from students where roll=%s",(roll,))
        student=cur.fetchone()
        if not student:
            print("Student Doesn't Exist with this roll number!!!")
            return 
        
        cur.execute("delete from students where roll=%s",(roll,))
        conn.commit()
        print("Student Data Deleted Sucessfully")
        print("-"*70)
    except Exception as e:
        print("Error:",e)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
        

def updateStudent():  # This function is used to update student info with help of roll number
    conn=None
    cur=None
    try:
        conn=get_connection()
        cur=conn.cursor()
        roll=int(input("Enter Roll Number:"))
        cur.execute("""select * from students where roll = %s""",(roll,))
        student=cur.fetchone()
        if not student:
            print("Student With This roll number doesn't exist")
            print("-"*70)
            return
        name=(input("Enter New Name:"))
        gender=(input("Enter Gender:"))
        degree=input("Enter Degree:")
        semester=int(input("Enter Semester:"))
        byear=int(input("Enter Birth Year:"))
        cur.execute("""Update students
                        set name=%s,
                        gender=%s,
                        degree=%s,
                        semester=%s,
                        byear=%s
                        Where roll=%s""",(name,gender,degree,semester,byear,roll))

        conn.commit()
        print("Student Updated Sucessfully")
        print("-"*70)
    except Exception as e:
        print("Error:",e)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
        

def displayAll():  # This program is used to display all students data
    conn=None
    cur=None
    try:
        conn=get_connection()
        cur=conn.cursor()
        cur.execute("Select * from students")
        allstudents=cur.fetchall()
        if not allstudents :
            print("Table is empty!")
            print("-"*70)
            return 
        print(f"{'Roll':<6}{'Name':<40}{'Gender':<10}{'Degree':<25}{'Semester':<10}{'Birth Year':<10}")
        print("-" * 100)

        print("-"*70)
        for s in allstudents:
            print(f"{s[0]:<6}{s[1]:<40}{s[2]:<10}{s[3]:<25}{s[4]:<10}{s[5]:<10}")
        print("-"*100)
    
    except Exception as e:
        print("Error:",e)
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()




# -------------------------Main Body------------------------------------



while (True):
    print("1. Enter a Student")
    print("2. Display Students Info")
    print("3. Update Student Info")
    print("4. Delete Student Info")
    print("5. Display All Students")
    print("6. Terminate Program")
    print("-"*70)
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
        print("="*70)
        break
