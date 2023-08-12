while True:
    try:
        x = int(input("What's x? "))
    except ValueError:                              # specify the error type, do not just omit "ValueError"!
        print("You haven't entered a number.")
    else:                                           # executed when no error is thrown
        break                                       # leaves the infinite while loop as soon as the assignment worked
    # finally:
        # print(f"You've entered {x}.")

print(f"x is {x}")


def main():
    x = get_int("What's x (I'm in the function)? ")
    print(f"x is {x}")


def get_int(prompt) -> int:
    while True:
        try:
            return int(input(prompt))                                   # breaks the loop implicitly
            # it's also valid to first assign it and then return; both ways are ok
        except ValueError:
            # print("You haven't entered a number.")
            pass                                                        # just goes back to the try


main()