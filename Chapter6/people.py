
taylor = {
    'first_name': 'taylor',
    'last_name': 'k1',
    'age': 7,
    'city': 'clarence',
}

alex = {
    'first_name': 'alex',
    'last_name': 'k2',
    'age': 5,
    'city': 'clarence',
}

shannon = {
    'first_name': 'shannon',
    'last_name': 'k3',
    'age': 39,
    'city': 'albion',
}

people = {
    'taylor': taylor,
    'alex': alex,
    'shannon': shannon,
}

for name, person in people.items():
    print("First name: " + person['first_name'])
    print("Last name: " + person['last_name'])
    print("Age: " + str(person['age']))
    print("City: " + person['city'])
    print("\n")