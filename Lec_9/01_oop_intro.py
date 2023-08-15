# approach: start with procedural/functional and simple examples, then optimize them via oop

def main():
    # name = get_name()
    # house = get_house()
    # name, house = get_student()  # also possible, but I changed to student to state it's a tuple coming back
    student = get_student()  # possible as the function returns a tuple (which is just a immutable(!) list(!))

    # if student["name"] == "Padma":
    #     student["house"] = "Ravenclaw"

    # print(f"{student[0]} from {student[1]}")
    print(f"{student['name']} from {student['house']}")


# def get_name():
#     return input("What's your name? ")
#
#
# def get_house():
#     return input("What's your house? ")


def get_student():
    # name = input("What's your name? ")
    # house = input("What's your house? ")

    # return (name, house)  # this returns a tuple (one value with two things inside of it; parentheses not needed!)

    # return [name, house]  # this would instead return a list (which would ofc be mutable)

    # student = {}
    # student["name"] = input("What's your name? ")
    # student["house"] = input("What's your house? ")
    # return student  # this returns a dict
    # alternative to the upper dict solution:
    name = input("What's your name? ")
    house = input("What's your house? ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()