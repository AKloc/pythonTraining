# Here's a function. Pretty straightforward. Indents are important, as usual.
# def greet_user():
#     print("Hello!")

# greet_user()


# With parameter...
# def greet_user(username):
#     print("Hello, " + username + "!")

# greet_user("Derp")


def greet_user(username):
    print("Hello, " + username + "!")

while True:
    name = input("What's your name? Enter 'quit' to quit. ")
    if name == 'quit':
        break
    greet_user(name)