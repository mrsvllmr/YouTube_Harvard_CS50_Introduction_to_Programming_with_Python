students = []

with open("names.csv", encoding="utf8") as file:
    for line in file:
        # read
        # row = line.rstrip().split(",")
        # print
        # print(f"{row[0]} lives in {row[1]}")
        # print(f"{name} lives in {place}")

        name, place = line.rstrip().split(",")
        # student = {}
        # student["name"] = name
        # student["place"] = place
        student = {"name": name, "place": place}
        students.append(student)

# students.append(f"{name} is in {place}")
# for name in sorted(students):
#     print(name)

# def get_name(student):      # expects a dict as input
#     return student["name"]

# anonymous lambda function replaces the need of get_name
# use lambda when you do not need it often and the function does not need a name
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['place']}")