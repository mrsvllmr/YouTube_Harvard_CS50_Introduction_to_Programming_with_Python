# create a dict on the fly

# WITHOUT DICT COMPREHENSION
students = ["Hermione", "Harry", "Ron"]

# gryffindors = []
#
# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})
#
# print(gryffindors)


# WITH DICT COMPREHENSION
# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]  # list comprehension
gryffindors = {student: "Gryffindor" for student in students}  # dict comprehension

print(gryffindors)
