students = ["Hermione", "Harry", "Ron"]

# SO FAR
for student in students:
    print(student)

for i in range(len(students)):
    print(i+1, students[i])

# ENUMERATE - enumerates over a sequence and gets both value and index
for i, student in enumerate(students):
    print(i+1, student)
