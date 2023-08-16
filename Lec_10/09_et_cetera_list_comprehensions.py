# construct a list on the fly (without loops/appends etc.)

def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = [word.upper() for word in words]  # Python expression within the list
    print(*uppercased)


if __name__ == "__main__":
    main()


#######################################################################################

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)
