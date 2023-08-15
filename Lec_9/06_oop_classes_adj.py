class Student:
    def __init__(self, name, house="Gryffindor"):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("What's your name? ")
        house = input("What's your house? ")
        return cls(name, house)  # instantiates a student object


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()