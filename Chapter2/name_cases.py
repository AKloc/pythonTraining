name = "Bobby secondname"
print("Hello " + name + ", would you like to learn some Python today?")

print("Uppercase: " + name.upper())
print("Lowercase: " + name.lower())
print("Titlecase: " + name.title())

print("Albert Einstein once said, \"A person who never made a mistake never tried anything new.\"")

famous_person = "Albert Einstein"
message = famous_person + " once said, \"A person who never made a mistake never tried anything new.\""
print(message)

# This adds a newline.
#message += " Let's add some whitespace at the end."

# Maybe this doesn't.
message = message + " Let's add some whitespace at the end.  "

message = "  And some leading whitespace. " + message
print("'" + message + "'")

print("Left Strip: '" + message.lstrip() + "'")
print("Right Strip: '" + message.rstrip() + "'")
print("Strip: '" + message.strip() + "'")