# generate values in Python from functions
# but they return just a little bit of that data at a time
# -> no longer too much getting returned all at once

def main():
    n = int(input("What's n? "))
    # for i in range(n):
        # print("🐑" * i)
        # print(sheep(i))
    for s in sheep(n):
        print(s)


# def sheep(n):  # works for a lot of data, but for instance no anymore for n=1000000 etc.
#     # return "🐑" * n
#     flock = []
#     for i in range(n):
#         flock.append("🐑" * i)
#     return flock

def sheep(n):  # works for a lot of data, but for instance no anymore for n=1000000 etc.
    for i in range(n):
        yield "🐑" * i  # return one value at a time ... return one value at a time ...
        # in this case returns one row of sheep at a time


if __name__ == "__main__":
    main()
