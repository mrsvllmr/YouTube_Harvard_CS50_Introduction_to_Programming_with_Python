# while loop
i = 3

while i != 0:
    print(f"{i} is still != 0")
    i -= 1


# for loop
for i in [0,1,2]:                               # iterate over list
    print(f"{i} is part of the list")

for i in range(3):
    print(f"{i} is within the defined range")   # notice: starts with 0

for _ in range(3):                              # name it _ when you don't care about the value or the variables name
    print(f"{i} is within the defined range")   # notice: starts with 0

print("meow\n" * 3, end="")                     # prints it three times, each on its own line


# user input should match a pattern (make use of an "infinite" loop)
while True:
    n = int(input("What's n? "))
    if n > 0:
        break                                   # leaves loop when n is greater than 0, otherwise asks again

for _ in range(n):
    print("meow")


# wrap it into a function
def main():
    number = get_number()
    meow(number)


def get_number() -> int:
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")


main()