name = "ada lovelace"
print(name.title())

name = name.upper()
print(name)

name = name.lower()
print(name)

first_name = "First"
second_name = "Word"

print(first_name + " " + second_name)

print("Hi, " + name.title() + "!")

string_with_whitespace = " leading and trailing whitespace. "

# This only strips the end of the whitespace.
print("'" + string_with_whitespace.rstrip() + "'")

# This strips the start of the whitespace
print("'" + string_with_whitespace.lstrip() + "'")

# How about both with method chaining.
print("'" + string_with_whitespace.lstrip().rstrip() + "'")

# How about both with this neat strip method.
print("'" + string_with_whitespace.strip() + "'")