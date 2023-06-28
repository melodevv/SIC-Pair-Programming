student_tup = [
    ('211101', 'David Doe', '010-123-1111'),
    ('211102', 'John Smith', '010-123-2222'),
    ('211103', 'Jane Carter', '010-123-3333')
]

student_num = input("Enter student number: ")
found = False

for student in student_tup:
    if student[0] == student_num:
        name = student[1]
        phone = student[2]
        found = True
        break

if found:
    print("Name:", name)
    print("Phone number:", phone)
else:
    print("Student number not found")