import re

url = input("URL: ").strip()
# print(url)

# assumption: user input will be sth like 'https://twitter.com/mrsvllmr'
# username = url.replace("https://twitter.com/", "")
# print(f"Username: {username}")

# username = url.removeprefix("https://twitter.com/")
# print(f"Username: {username}")

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")

matches = re.search(r"^https?://(?:www\.)?twitter\.com/([\w]+)$", url, re.IGNORECASE)  # (.+) captures the username
if matches:
    print(f"Username: {matches.group(1)}")
    # either matches.group(2), because of the (www\.) capture!
    # or non-capturing the subdomain by using (?:www\.)