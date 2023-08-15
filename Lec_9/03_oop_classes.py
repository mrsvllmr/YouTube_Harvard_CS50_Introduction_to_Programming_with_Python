# patronus and other lines again removed to focus on other class functionalities
class Student:  # this already invents a new datatype/class (without any attributes etc.)
    def __init__(self, name, house="Gryffindor"):  # instance method for initializing an object; default value defined
        # conditional instantiation (later moved to the setter function)
        # if not name:
        #     raise ValueError("Missing name")
        self.name = name  # instance variable
        self.house = house  # instance variable; reminder: setter will automatically be called here also

    def __str__(self):  # automatically used when trying to print a Student object
        return f"{self.name} from {self.house}"

    @property # marks a getter
    def name(self):
        return self._name

    @name.setter  # marks a setter; will be called whenever you try to assign sth; includes input validation
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property  # marks a getter
    def house(self):
        return self._house

    @house.setter  # marks a setter; will be called whenever you try to assign sth; includes input validation
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    # student.house = "Number Four, Privet Drive"  # will not automatically call the setter function above
    # the upper line will not work due to the input validation, but the next will!
    # convention: never ever assign sth to the instance variables, marked as _name!!!
    # student._house = "Number Four, Privet Drive"
    print(student)


def get_student():

    name = input("What's your name? ")
    house = input("What's your house? ")
    return Student(name, house)  # calls the constructor defined above (instantiates the object)


if __name__ == "__main__":
    main()