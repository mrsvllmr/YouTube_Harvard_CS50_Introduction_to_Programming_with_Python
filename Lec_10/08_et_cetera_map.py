# map --> apply some function to every element of a list

# WITHOUT MAP:
# def main():
#     yell("This", "is", "CS50")
#
#
# def yell(*words):
#     uppercased = []
#     for word in words:
#         # print(word, end="")
#         uppercased.append(word.upper())
#     print(*uppercased)
#
#
# if __name__ == "__main__":
#     main()


def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()
