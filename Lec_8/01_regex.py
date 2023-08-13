import re

email = input("What's your email? ").strip()

# contains an @?

# first approach
# if "@" and "." in email:
#     print("Valid")
# else:
#     print("Invalid")

# second approach
# username, domain = email.split("@")
#
# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")

# third approach: using the re library
#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.com$", email): # r in the beginning works as escaping backslash
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(com|de|org)$", email, re.IGNORECASE):  # \w replaces the whole expression above
    print("Valid")
else:
    print("Invalid")

# pattern above accepts usernames with word characters and dots
# pattern above accepts an optional subdomain -> (\w+\.)?

##################################
# . any character except a newline
#
# * 0 or more repetitions
# + 1 or more repititions
# ? 0 or 1 repitition
# {m} m repititions
# {m,n} m-n repititions
#
# ^ matches the start of the string
# $ matches the end of the string
#
# [] set of characters
# [^] complementing the set
#
# \w word character and numbers and underscores
# \W not a word character
# \d decimal digit
# \s whitespace characters
# \S not a whitespace character
#
# A|B either A or B
# (...) a group
# (?:...) non-capturing version
##################################

# other functions in re:
# re.match()
# re.fullmatch()