# write a Python program to create an instance of a specified class and display the namespace of the said instance.

class Student:
    def __init__(self, student_id, student_name, class_name):
        self.student_id = student_id
        self.student_name = student_name
        self.class_name = class_name

stu = Student(1, "John", "Python")
stu1 = Student(2, "Mary", "Java")
print(stu1.__dict__)