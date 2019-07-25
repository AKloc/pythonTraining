# Opening files.

# open() will open a file.
# "with" is the rough equivalent of "using" in C# in that it will close out
#   the file and dispose of everything else within its purview.

# Had to use the fully qualified name to get here, probably because the path
#   of the python files we're running are being passed in and python isn't
#   being run from the same directory as the source files.
with open("C:\\repos\\pyTraining\\Chapter10\\pi_digits.txt") as file_object:
    contents = file_object.read()
    # contents includes the line breaks, this isn't a loop or anything.
    print("Contents: " + contents.rstrip()) # get rid of the trailing newline.



# Let's read line by line.
with open("C:\\repos\\pyTraining\\Chapter10\\pi_digits.txt") as file_object:
    for line in file_object:
        print("Here's a line: " + line.rstrip()) #Definitely need to use rstrip.

pi_string = ""

# How about putting the contents in a list?
with open("C:\\repos\\pyTraining\\Chapter10\\pi_digits.txt") as file_object:
    lines = file_object.readlines()
    print("Lines is size:" + str(len(lines)))
    for line in lines:
        pi_string += line.rstrip()
        print("Here's a line in the list: " + line.rstrip()) #Definitely need to use rstrip.

print("Whole string without spaces: " + pi_string)