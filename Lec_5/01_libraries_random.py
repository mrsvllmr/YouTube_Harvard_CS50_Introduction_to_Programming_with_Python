# a module in Python is just a library
# goal: encourage reusability of code

import random                                       # imports the whole module
from random import choice
from random import randint


# https://docs.python.org/3/library/random.html
list = [1, 2, 3, 4, 5, 6]
list2 = ["heads", "tails"]

# print(random.choice(list))                          # expects a sequence
# print(random.choice(list2))

print(choice(list))                                   # no more need to write random because of from ... import ...
print(choice(list2))                                  # be aware of name conflicts!

number = randint(1,10)
print(number)

random.shuffle(list)
print(list)