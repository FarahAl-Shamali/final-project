"""ITF 07 Final Project Attendance System
# TODO 1 Enter your name and submission date
Name : Farah Al_Shamali
Delivery Date : 22/6/2023
"""
import uuid

# TODO 2 Define Course Class and define constructor with
# course_id (generated using uuid4) ,
# course name (user_input) and
# course mark (user_input)
class Course:
    def _init_(self):
        self.course_id = str(uuid.uuid4())
        self.course_name =''
        self.course_mark = 0


class Student:
    # TODO 3 define static variable indicates total student count

    std_count = 0

    # TODO 4 define a constructor which includes
    # student_id (unique using uuid module)
    # student_name (user input)
    # student_age (user input)
    # student_number (user_input)
    # courses_list (List of Course Objects)
    def __init__(self, std_name, std_age, std_num):
        Student.std_count += 1
        self.student_id = str(uuid.uuid4())
        self.student_name = std_name
        self.student_age = std_age
        self.student_number = std_num
        self.courses_list = []

    # TODO 5 define a method to enroll new course to student courses list
    def enroll_course(self, c_name, c_mark):
        cou = Course()
        cou.course_name = c_name
        cou.course_mark = c_mark
        self.courses_list.append(cou)

    # method to get_student_details as dict
    def get_student_details(self):
        return self.__dict__

    # method to get_student_courses
    def get_student_courses(self):
        # TODO 6 print student courses with their marks
        for i in courses_list:
            print(f'course is: {self.course_name} and the course mark is{self.course_mark}')
            print()

    # method to get student_average as a value
    def get_student_average(self):
        # TODO 7 return the student average
        sum = 0
        average = 1.0
        for course in self.courses_list:
            sum += course.course_mark
        average = sum / len(self.courses_list)
        return average


# in Global Scope
# TODO 8 declare empty students list
students_list = []

while True:

    # TODO 9 handle Exception for selection input
    while True:

      try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit"))
        if 1 <= selection <= 6:
            break
        elif selection > 6:
            print('Enter a valid number:')
            True
      except NameError:
        print("please enter a number between 1 and 6:")

    if selection == 1:

        # TODO 10 make sure that Student number is not exists before
        student_number = int(input("Enter Student Number"))
        while any(student.student_number == student_number for student in students_list):
            print('Number a;ready exists Please enter another number:')
            student_number = int(input('Enter Student Number:'))

        student_name = input("Enter Student Name")
        while True:
            try:
                student_age = int(input("Enter Student Age"))
                break
            except:
                print("Invalid Value")

        # TODO 11 create student object and append it to students list
        std = Student(student_name, student_age, student_number)
        students_list.append(std)
        print("Student Added Successfully")

    elif selection == 2:
        std_num = int(input("Enter Student Number"))
        # TODO 12 find the target student using loops and delete it if exist , if not print ("Student Not Exist")
        isFound = False
        for std in students_list:
            if std.student_number == std_num:
                students_list.remove(std)
                isFound = True
                break
        if isFound:
            print('Task deleted successfully')
        else:
            print('Student Does Not Exist')

    elif selection == 3:
        std_num = int(input("Enter Student Number"))
        # TODO 13 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")
        isFound = False
        for std in students_list:
            if std.student_number == std_num:
                print(f"student id ={std.student_id}")
                print(f"student number ={std.student_number}")
                print(f"student name is{std.student_name}")
                print(f"student age is{std.student_age}")
                isFound = True
                break
        if not isFound:
            print('Student DOes Not Exist')



    elif selection == 4:
        std_num = int(input("Enter Student Number"))
        # TODO 14 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")
        isFound = False
        for std in students_list:
            if std.student_number == std_num:
                av = std.get_student_average()
                print(f'average= {av}')
                isFound = True
                break
            if not isFound:
                print('Student Does Not Exist')

    elif selection == 5:
        isFound = False
        std_num = int(input("Enter Student Number"))
        # TODO 15 ask user to enter course name and course mark then create coures object then append it to target student courses
        for std in students_list:
            if std.student_number == std_num:
                c_name = input('Enter the name of the course:')
                c_mark = int(input('Enter the mark of the course:'))
                std.enroll_course(c_name, c_mark)
                break
            if not isFound:
                print('Student Does Not Exist')

    else:
        # TODO 16 call a function to exit the program
        exit()
