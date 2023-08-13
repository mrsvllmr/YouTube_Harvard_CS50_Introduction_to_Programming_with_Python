names = []

# ask three times and append to list
for _ in range(3):
    name = input("What's your name? ")
    names.append(name)

# print the sorted list
for name in sorted(names):
    print(f"Hello, {name}")

# open the file with append mode and write the element to the file
# file = open("names.txt", "a")
# for name in sorted(names):
#     file.write(f"{name}\n")
# file.close()

# alternative for opening a file
with open("names.txt", "a") as file:    # automatically closes the file
    for name in sorted(names):
        # file.write(f"{name}\n")
        pass

# read the content of the file
with open("names.txt", "r") as file:    # r is default
    for line in file:
        names.append(line.rstrip())

# print the sorted list
for name in sorted(names):
    print(f"hello, {name}")

# you can basically just sort the file itself (easier)
with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())