# int
# Casting (in this case to int in order to be able to calculate)
x = int(input("First number: "))
y = int(input("Second number: "))

print(x + y)

# float
x = float(input("First float value: "))
y = float(input("Second float value: "))

# round
print(round(x + y, 1))

# formatting (separators)
formattedResult = round(x + y)
print(f"{formattedResult:,}")

# division
z = round(x / y, 2)
print(z)

print(f"{z:.2f}")  # rounding by using an f-String
