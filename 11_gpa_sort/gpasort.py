# Debra Sparr
# 4/11/21
# Assignment 11 - GPA Sort

from gpa import *


def readStudents(file):
    with open(file, 'r') as f:
        students_list = []
        for stu in f:
            students_list.append(makeStudent(stu))
        f.close()
        return students_list

def sort_gpa(stu_list:list):
    return stu_list.gpa()

def sort_name(stu_list:list):
    return stu_list.name

def sort_credit(stu_list:list):
    return stu_list.hours

def write_file(file, stu_list:list):
    with open(file, 'w+') as f:
        for i in stu_list:
            f.write(i.__str__())
            f.write('\n')
        f.close()

def start_prompt():
    ''' Allows the user to sort a file of students based on GPA, name, or credit.
        User also defines a file to write the result to. '''
    filename = input('Enter path to file with student information : \n')
    student_list = readStudents(filename)
    sort_field = input('Sort student by : \n a) GPA \n b) name \n c) credits \n')
    write_to_file = input('Enter name of file you would like to write to : \n')
    if sort_field == 'a':
        sorted_stu = sorted(student_list, key=sort_gpa)
        write_file(write_to_file, sorted_stu)
    if sort_field == 'b':
        sorted_stu = sorted(student_list, key=sort_name)
        write_file(write_to_file, sorted_stu)
    if sort_field == 'c':
        sorted_stu = sorted(student_list, key=sort_credit)
        write_file(write_to_file, sorted_stu)

if __name__ == '__main__':
    start_prompt()
