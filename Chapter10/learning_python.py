# r in front of quotes for "Raw"
filename = r"C:\Users\andyk\source\repos\pyTraining\Chapter10\learning_python.txt"

file_contents = []

with open(filename) as file_object:
    print(file_object.read())

    for line in file_object:
        print(line)
    

with open(filename) as file_object:
    file_contents = file_object.readlines()
    
print(file_contents)