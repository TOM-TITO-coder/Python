# write a pythoon class named Student with instances student1, student2 and assign values to the instances' attributes. Print all the attributes of the student1, student2 instances with their values in the given format.

# class Student:
#     school = 'Institute of Technology of Cambodia'
#     address = 'Russian Federation Blvd, Phnom Penh'
# student1 = Student()
# student2 = Student()
# student1.student_id = 'e20200061'
# student1.student_name = 'Tito'

# write a python class named Student with two atrributes: student_id, student_name. Add a new attribute: student_clss. 
# Create a function to display all attributes and their values in the Student class.

class Student:
    student_id = 'e20200061'
    student_name = 'Tito'
    def display():
        print(f'Student id: {Student.student_id}\nStudent naem: {Student.student_name}')

Student.display()
print("Original: ")
Student.student_class = 'Python'

Student.display = staticmethod(lambda: print(f'Student id: {Student.student_id}\nStudent naem: {Student.student_name}\nStudent class: {Student.student_class}'))

print("After adding student_class: ")
Student.display()

