class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name


class Student(Wizard):  # Student is a sublass of Wizard (Wizard is the superclass)
    def __init__(self, name, house):
        super().__init__(name)  # reference to the superclass, here Wizard
        self.house = house

    ...


class Professor(Wizard):  # Professor is a sublass of Wizard (Wizard is the superclass)
    def __init__(self, name, subject):
        super().__init__(name)  # reference to the superclass, here Wizard
        self.subject = subject

    ...


wizard = Wizard("Albus")
student = Student("Harry","Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
