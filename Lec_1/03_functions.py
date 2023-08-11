# Ask user for their name
# parameterize the function call
# make use of a main function in order to be independent of the order of the file contents
def main():
    inputname = input("What's your last name? ").strip().title()
    sayhello(inputname)
    sayhello()  # will make use of the default value

# define your own function
def sayhello(name="world"):  # parameter with a default value
    # Say hello to the user
    print(f"Hello, {name}")


main()