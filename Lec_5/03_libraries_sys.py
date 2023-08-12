import sys

# try:
#     print("hello, my name is", sys.argv[1])     # index 0 references the file name
# except IndexError:
#     print("You did not tell me your name. My argv list is empty.")

# # Check for errors
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")           # will exit the program in case of this condition/error
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")          # will exit the program in case of this condition/error
#
# # Print name tags
# print("Hello, my name is", sys.argv[1])     # will only be reached in case of no errors above due to exit()

# Check for errors
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:                      # list slicer prevents printing the name of the file (index 0)
    print(arg)

for arg in sys.argv[1:-1]:                    # list slicer also work coming from the end of the list
    print(arg)