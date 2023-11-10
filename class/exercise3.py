# write a python class named Student with two attributes 
# student_id , student_name. add a new attribute student_class and display the entire attribute and the values of the class.
# now remove the student_name attribute and display the entire attribte with values.

class Student:
    student_id = 'e20200061'
    student_name = 'Tito'

print("Original attributes and their values of the Student class:")
for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')

print("\nAfter adding the student_class, attributes and their values with the said class: ")
Student.student_class = 'Python'

for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')
        
print("\nAfter removing the student_name, attributes and their values with the said classs: ")
del Student.student_name   # delete the student_name attribute

for attr, value in Student.__dict__.items():
    if not attr.startswith('_'):
        print(f'{attr} -> {value}')


    