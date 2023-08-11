x = int(input("What's x? "))
y = int(input("What's y? "))

# if x < y:                                     # if
#     print("x is less than y")
# elif x > y:                                   # elif
#     print("x is greater than y")
# else:                                         # else
#     print("x is equal to y")

# if x < y or x > y:                            # or
#     print("x is not equal to y")
# else:
#     print("x is equal to y")

score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:  # you implicitly know it's in between
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print(f"{x} is even")
    else:
        print(f"{x} is odd")

    usemap()


def is_even(n) -> bool:
    # if n % 2 == 0:                              # first option
    #     return True
    # else:
    #     return False

    # return True if n % 2 == 0 else False        # second option: pythonic way to prevent if else etc.

    return n % 2 == 0                             # third/best option:
    # even shorter and same result as it already will be bool


def usemap():
    name = input("What's your name? ")

    match name:                                   # map (function similar to switch in other languages)
        case "Harry" | "Hermine" | "Ron":         # shorter syntax when having many values
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _:                                   # for cases that have not been handled
            print("Who?")


main()