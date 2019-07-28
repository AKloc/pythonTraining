import json

filename = r'Chapter10\numbers.json'
numbers = []
with open(filename, 'r') as f_obj:
    numbers = json.load(f_obj)

print(numbers)