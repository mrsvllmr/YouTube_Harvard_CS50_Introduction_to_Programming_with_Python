# constants are not actually enforced by Python

MEOWS = 3  # convention for constants (but again, not forced)
# MEOWS = 4  # this would still work, so technically it is not a constant

for _ in range(MEOWS):
    print("meow")
print()


##########################################################################


class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")


cat = Cat()
cat.meow()
