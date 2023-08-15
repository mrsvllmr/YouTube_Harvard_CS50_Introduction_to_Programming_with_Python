# program for checking whether your code is adhering to your type hints: mypy -> pip install mypy

def meow(n: int) -> str:  # notice: type hint for the parameter and for the return value
    # for _ in range(n):  # (they are also not enforced by the language as Python is dynamically typed)
    #     print("meow")
    # print()
    return "meow\n" * n  # reminder: * also overloaded for strings


number: int = int(input("Number: "))  # another type hint, in this case for the variable itself
# meow(number)

meows: str = meow(number)  # I accidentally expect that meow returns a string
print(meows, end="")  # I accidentally expect that meow returns a string
# -> will instead just print None, because the function does not return a string or anything else
# we changed the return value to str afterwards

# we than ran "mypy .\04_et_cetera_type_hints.py"
