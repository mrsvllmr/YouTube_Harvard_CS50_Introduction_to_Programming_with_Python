# Ask user for their name
name = input("What's your name? ")

# Say hello to user
# Concatenation
print("hello, " + name)
print("hello,", name)  # automatically inserts a space in between; parameter: sep=' '
print("hello, 'friend'")  # rule: be consistent regarding the quotes (inside/outside)

# Escaping
print("hello, \"friend\"")  # by using \ as the escape character

# Function parameters (end/sep) and f-String
print(f"hello, {name}", end=" ")  # automatically would insert a new line; parameter: end='\n'
print("...now the text continous on the same line.")

# Functions/Methods of str
# Remove whitespaces from str
stringWithoutWhitespace = name.strip()
print(f"without Whitespace, {stringWithoutWhitespace}")

# Capitalize user's name
stringCapitalized = stringWithoutWhitespace.capitalize()
print(f"capitalized, {stringCapitalized}")

# Title (capitalize first character of each word) user's name
stringTitled = stringCapitalized.title()
print(f"titled, {stringTitled}")

# Remove whitespaces AND title user's name
stringWithoutWhitespaceAndTitled = name.strip().title()
print(f"without Whitespace AND titled, {stringWithoutWhitespaceAndTitled}")

# Split user's name into first name and last name
first, last = name.split(" ")
print(f"hello, mr {last}")