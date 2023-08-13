import re

# name = input("What's your name? ").strip()
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"hello, {name}")

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), ?(.+)$", name)  # () captures here (no grouping as seen with match!)
if matches:
    # first approach
    # last, first = matches.groups()
    # name = f"{first} {last}"

    # second approach
    # last = matches.group(1)
    # first = matches.group(2)
    # name = f"{first} {last}"

    # third approach
    name = f"{matches.group(2)} {matches.group(1)}"

print(f"hello, {name}")

# difference to the first file of this chapter:
# we are using the return value of the search function by capturing them in ()

# also possible: assignment and asking a boolean question
# if matches := re.search(r"^(.+), ?(.+)$", name):