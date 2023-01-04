


def initial_display():
    display='''\tSunway Int'l College Grading System
                    Maitidevi,Kathmandu
        .....*.....*.....*.....*.....*.....*.....'''
    print(display)
#Calculation part
def calculation(sub1,sub2,sub3,sub4,sub5):
    per=((sub1)+(sub2)+(sub3)+(sub4)+(sub5))/(5*100) *100
    print(per)
    print(sub1,sub2,sub3,sub4,sub5)
    if(per>90 and per<=100):
        Grade="A+"
        print(Grade)
    elif(per>80 and per<=90):
        Grade="A"
        print(Grade)
    elif(per>70 and per<=80):
        Grade="B+"
        print(Grade)
    elif(per>60 and per<=70):
        Grade="B-"
        print(Grade)
    elif(per>50 and per<=60):
        Grade="B"
        print(Grade)
    elif(per>40 and per<=50):
        Grade="C+"
        print(Grade)
    elif(per>30 and per<=40):
        Grade="D"
        print(Grade)
    elif(per>20 and per<=30):
        Grade="E"
        print(Grade)    
    else:
        Grade="F"
        print(Grade)
        print(Grade)
    return Grade

#Final Display
def display_information(Student_name,Student_address,Student_faculty,Student_program,Student_intake,Grade):
    print(f"Student Name:{Student_name}\tStudent Address:{Student_address}")
    print(f"Student Faculty:{Student_faculty}\tStudent Program :{Student_program}")
    print(f"Student Intake:{Student_intake}\tStudent Grade: {Grade}")

#Info display
def iformation_display():
    Std_no=int(input("Enter number of students: "))
    Student_name=[]
    Student_address=[]
    Student_faculty=[]
    Student_program=[]
    Student_intake=[]
    sub1=[]
    sub2=[]
    sub3=[]
    sub4=[]
    sub5=[]
    grade=[]
    for i in range(Std_no):
        Student_name.append(input(f"Enter name of student[{i+1}]: "))
        Student_address.append(input(f"Enter address of student[{i+1}]: "))
        Student_faculty.append(input(f"Enter faculty of student[{i+1}]: "))
        Student_program.append(input(f"Enter program of student[{i+1}]: "))
        Student_intake.append(input(f"Enter intake of student[{i+1}]: "))
        sub1.append(int(input(f"Enter marks for sub1[{i+1}]: ")))
        sub2.append(int(input(f"Enter marks for sub2[{i+1}]: ")))
        sub3.append(int(input(f"Enter marks for sub3[{i+1}]: ")))
        sub4.append(int(input(f"Enter marks for sub4[{i+1}]: ")))
        sub5.append(int(input(f"Enter marks for sub5[{i+1}]: ")))
    g=calculation(sub1[i],sub2[i],sub3[i],sub4[i],sub5[i])
    grade.append(g)

    for i in range(Std_no):
        initial_display()
        display_information(Student_name[i],Student_address[i],Student_faculty[i],Student_program[i],Student_intake[i],grade[i])

iformation_display()