magicians = ['alice', 'david', 'carolina']

# Note the colon at the end. Required.
for magician in magicians:
    # This indentation matters! Indent can be any size (I tried tab and single space)
    print(magician.title() + ", that was a great trick!")
    print("Because this line is indented, it will run in the for loop.\n")
print("This line is NOT indented and won't run in the loop.")

# More on indentation... indenting for no reason also causes failures!
# The below would throw an "unexpected indent" error.

#   message = "Hi"
# print(message)