# Learning input(). It takes a prompt parameter.
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)


# Now let's use a while loop. Note - have to define the meessage variable in advance.
# message = ""
# while message != "quit":
#     message = input("Tell me something, and I will repeat it back to you: ")
#     print(message)

# Do it again, but this time use a flag.
# message = ""
# flag = True
# while flag:
#     message = input("Tell me something, and I will repeat it back to you: ")
#     print(message)
#     if message == 'quit':
#         flag = False

# Do it AGAIN, but this time use a break.
# message = ""
# while True:
#     message = input("Tell me something, and I will repeat it back to you: ")
#     print(message)
#     if message == 'quit':
#         break

# Do it AGAIN, but this time use a break and a continue.
message = ""
while True:
    message = input("Tell me something, and I will repeat it back to you: ")
    if message == 'quit':
        break
    elif message == 'continue':
        continue
    else:
        print(message)    