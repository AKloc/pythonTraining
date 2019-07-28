import json

def write_favorite_number():
    favorite_number = input("What's your favorite number?")
    filename = r"Chapter10\FavoriteNumber.json"
    with open(filename, 'w') as file_obj:
        json.dump(favorite_number, file_obj)

def read_favorite_number():
    filename = r"Chapter10\FavoriteNumber.json"
    with open(filename, 'r') as file_obj:
        favorite_number = json.load(file_obj)
        print("Your favorite number is " + favorite_number)

try:
    read_favorite_number()
except FileNotFoundError:
    print("The file doesn't exist yet.")

write_favorite_number()
read_favorite_number()