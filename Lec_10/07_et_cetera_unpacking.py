# unpacking means to unpack a single value into two variables or similar

# first, last = input("What's your name? ").split(" ")  # first approach naively
# print(f"hello, {first}")

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

# list
# print(total(100, 50, 25), "Knuts")
# print(total(coins[0], coins[1], coins[2]), "Knuts")
print(total(*coins), "Knuts")  # the * unpacks the sequence of coins within the list

# dict
print(total(galleons=100, sickles=50, knuts=25), "Knuts")  # keys and values --> dict better
coins = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")
print(total(**coins), "Knuts")  # unpacks the dict in this case (three key-value pairs) -> same as line 18


def f(*args, **kwargs):  # takes variable number of positional arguments and keyword arguments (named parameters)
    """fmi: also see *args, **kwargs use the same syntax"""
    print("Positional:", args)
    print("Keyword:", kwargs)


f(100, 50, 25, 5)  # returns a sequence
f(galleons=100, sickles=50, knuts=25)  # returns a dict
