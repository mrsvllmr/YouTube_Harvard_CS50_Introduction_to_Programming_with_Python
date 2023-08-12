def main():
    hello("Marius")
    goodbye("Marius")


def hello(name):
    print(f"Hello, {name}")


def goodbye(name):
    print(f"Goodbye, {name}")


if __name__ == "__main__":  # when you run a file from the cli
    main()  # so will not be executed when called from another file
