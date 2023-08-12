print("#")
print("#")
print("#\n")

for _ in range(3):
    print("#")
print()


def main():
    x = int((input("How high? ")))
    y = int((input("How long? ")))
    buildwall(x)
    buildline(y)
    print_square(x)


def buildwall(height):
    for _ in range(height):
        print("#")


def buildline(length):
    # for _ in range(length):
    #     print("#", end="")
    print("?" * length)                     # shorter, needs no loop!


def print_square(n):
    print()
    for _ in range(n):                      # for each row...
        # for _ in range(n):                # for each column...
        #     print("#", end="")            # print brick
        # print()                           # go to next line

        # print("#" * n)                    # much shorter as it replaces an inner loop

        print_row(n)


def print_row(n):
    print("#" * n)


main()