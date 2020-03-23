#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 18:27:57 2020

@author: wazir
"""

import datetime
import sys, os 

class Course:
    def __init__(self):
        self.course = []

class Student(Course):
    def __init__(self, name, course):
        self.name = name
        self.course = course
        
    def getStudentName(self):
        print(self.name)
        

class Enrollment(Student, Course):
    def __init__(self, date = datetime.datetime.now()):
        super(Enrollment, self).__init__(date = datetime.datetime.now())
        self.EnrollmentDate = date
        
    def enroll(self, course):
        for i in self.course:
            if(i == course):
                return None
        self.course.append(course)
        
    def drop(self, course):
        for i in self.course:
            if ( i == course):
                self.course.remove(course)
    
    def cancel(self):
        pass

student_name = ''
student = ''
enrollStudent = ''

def DisplayMenu():
    os.system('clear')
    choice = 0
    
    while (choice != '1' and choice != '2' and choice != '3'):
        print ("Main menu, please choose correct option. \n")
        print ("1. Create Student and Course.")
        print ("2. Enroll to course.")
        print ("3. Drop course.")
        choice = input(" >>  ")
    
    
    if(choice == '1'):
        
        createStudentCourse()
    elif(choice == '2'):
        enrollToCourse()
    elif(choice == '3'):
        dropEnrollment()
        
def createStudentCourse():
    student_name = input(" Please enter student name: ")
    student_age = input(" Please enter student age: ")
    while(student_age < '18'):
        student_age = input("Please enter a valid age:")
        
    student_course = input(" Please enter course name: ")
    
    student = Student(student_name, student_course)
    print(student.getStudentName())
    DisplayMenu()
    
def enrollToCourse():
    enrollStudent = Enrollment()
    enrollStudent.enroll(student.self.course)
    DisplayMenu()

def dropEnrollment():
    DisplayMenu()
    pass
    
    

if __name__ == "__main__":
    DisplayMenu()
    