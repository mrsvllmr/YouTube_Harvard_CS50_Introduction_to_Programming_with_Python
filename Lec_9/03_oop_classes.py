class Student:  # this already invents a new datatype/class (without any attributes etc.)
    def __init__(self, name, patronus, house="Gryffindor"):  # instance method for initializing an object; default value defined
        # conditional instantiation
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name  # instance variable
        self.house = house  # instance variable
        self.patronus = patronus

    def __str__(self):  # automatically used when trying to print a Student object
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russel terrier":
                return "🐕"
            case _:  # default case
                return "🪄"


def main():
    student = get_student()
    # print(f"{student.name} from {student.house}")
    # print(student)
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    # student = Student()
    # student.name = input("What's your name? ")
    # student.house = input("What's your house? ")
    # return student

    name = input("What's your name? ")
    house = input("What's your house? ")
    patronus = input("What's your patronus? ")
    return Student(name, patronus, house)  # calls the constructor defined above (instantiates the object)


if __name__ == "__main__":
    main()