import random


class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]  # class variable!

    @classmethod  # class method, used with the class itself (no instantiation)
    def sort(cls, name):  # convention: cls for class (instead of self for instance methods)
        print(name, "is in", random.choice(cls.houses))  # will pick a random house for us


# hat = Hat()  # instantiating an object of Hat
# hat.sort("Harry")
Hat.sort("Harry")