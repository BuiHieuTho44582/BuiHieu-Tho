"""
    Name: Bui Hieu Tho
    Date: 30/10/2021
    File: example_student_class.py
    Resources to manage a student's name and test scores
"""
from student import Student

if __name__ == '__main__':

    print(help(Student))

    student_a = Student("Võ Viết Thanh", 5)
    print("Name: ", student_a.getname())
    print("Score: ", student_a.getscores())
    print("Score in i: ", student_a.getscores(2))

    student_a.setscore(1, 9.0)
    print("Score in i: ", student_a.getscores(1))

    print("========"*10)
    print(student_a)
