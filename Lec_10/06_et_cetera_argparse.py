# import sys
#
# if len(sys.argv) == 1:
#     print("meow")
# elif len(sys.argv) == 3 and sys.argv[1] == "-n":
#     n = int(sys.argv[2])
#     for _ in range(n):
#         print("meow")
#
# else:
#     print("usage: meows.py")

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")  # constructor for the class
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()  # looks at sys.argv automatically

for _ in range(args.n):
    # n is automatically int because of the type defined above (add_argument)
    # n contains the user input number for the times to meow
    print("meow")
