# write a Python function student_data() that will print the ID of a student (student_id).
# if the user passes an argument student_name or student_class the function will print the student name adn class

def student_dat(student_id, **kwargs):
    print(f"\nStudent ID: {student_id}")
    if 'student_name' in kwargs:
        print(f"Student Name: $ {kwargs['student_name']}")
    
    if 'student_name' and 'student_class' in kwargs:
        print(f"\nStudent Class:$ {kwargs['student_class']}")
        print(f"Student Name:$ {kwargs['student_name']}")

student_dat(student_id='1', student_name="John", student_class="Python")
student_dat(student_id='2', student_name="Mary")
student_dat(3)
