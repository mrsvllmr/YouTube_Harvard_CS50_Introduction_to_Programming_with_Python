# lists
students = ["Hermione", "Harry", "Ron"]         # list of length 3

for student in students:                        # notice: you don't need an index!
    print(student)                              # additionally you don't need to initialize too!

for i in range(len(students)):                  # notice: you still need range, len is not sufficient!
    # print(i)
    # print(students[i])                        # notice: you can now address the elements via index
    print(i+1, students[i])


# dicts                                         # key-value pairs
houses = {
            "Gryffindor": ["Hermione", "Harry", "Ron"],
            "Slytherin": ["Draco"]
         }

print(houses)
print(houses["Gryffindor"])
print(houses["Gryffindor"][2])
print(len(houses["Gryffindor"]))

for house in houses:
    print(house)
    for student in houses[house]:
        print(student)


students = [                                    # dicts within a list - collections of values
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

print("\n### Beginning of dicts within a list ###")
for student in students:
    print(student["name"])