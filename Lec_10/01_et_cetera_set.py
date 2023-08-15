# datatype set, which is a list without duplicates

# list of students which dict in it
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

# goal: identify the unique houses
# houses = []
# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])
#
# for house in sorted(houses):
#     print(house)

houses = set()
for student in students:
    houses.add(student["house"])  # notice: add() instead of append() for sets; duplicates removed automatically

for house in sorted(houses):
    print(house)