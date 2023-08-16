def meow(n: int) -> str:
    # """Meow n times."""  # will lead to automatically created documentation
    # following adheres to a third party convention to create documentation automatically
    """
    Meow n times.
    :param n: Number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
