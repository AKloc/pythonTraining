#name = input("Please enter your name: ")
#print ("Hello, " + name)

# How about a multiline prompt? Exactly as you'd expect.
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("Hello, " + name + "!")

# Unsurprisingly, you have to convert a string to a number if that's what you want.
age_input = input("How old are you? ")

double_age = int(age_input) * 2

print("2x your age, you'd be " + str(double_age) + " years old.")
