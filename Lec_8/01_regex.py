email = input("What's your email? ").strip()

# contains an @?
if "@" and "." in email:
    print("Valid")
else:
    print("Invalid")