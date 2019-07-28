user_name = ""
while True:
    user_name = input("Please enter your name: ")
    if user_name == "quit":
        break

    filename = r"Chapter10\guest.txt"

    with open(filename, 'a') as file_object:
        file_object.write(user_name + "\n")