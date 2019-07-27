
filename = "C:\\repos\\pyTraining\\_CourseFiles\\chapter_10\\pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()
    print("There are " + str(len(lines))+ " lines in the file.")
    pi_string = ""
    for line in lines:
        pi_string += line.strip()
    print(pi_string[:52] + "...")
    print(len(pi_string))
    birthday = input("Enter your birthday, in the form mmddyy: ")
    if birthday in pi_string:
        print("Your birthday appears in the first million digits of pi!")
    else:
        print("Your birthday does NOT appear in the first million digits of pi.")