import csv

students = []

# reader
with open("names.csv", encoding="utf8") as file:
    # for line in file:
    #     name, place = line.rstrip().split(",")
    #     student = {"name": name, "place": place}
    #     students.append(student)
    reader = csv.reader(file, delimiter=",")

    # for row in reader:  # returns a row, but as a list!
    #     students.append({"name": row[0], "home": row[1]})
    for name, place in reader:  # returns a row, but as a list!
        students.append({"name": name, "place": place})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['place']}")


# DictReader
with open("nameswithheaders.csv", encoding="utf8") as file:
    # reads each line as a dict, not as a list
    reader = csv.DictReader(file, delimiter=",")
    for row in reader:
        students.append({"name": row["name"], "place": row["place"]})

print("\nNames with headers")
students.clear()  # to only see the effect of DictReader now
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['place']}")


# write to a csv file
# writer
studentstowrite = []

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

# dictwriter
studentstowrite = []

name = input("What's your name? ")
home = input("Where's your home? ")

with open("studentsdictwriter.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})