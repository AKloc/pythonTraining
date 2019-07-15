glossary = {
    'if': 'Lets you fork logic.',
    'dictionary': 'Key-value pair.',
    'array': 'Standard 2d array.',
    'for': 'Tighter foreach loop.',
    'else': "Logic thingy because I'm running out of ideas."
}

# Iterating through the dictionary. The .items() and "key" / "value" thing are 
#   brand new. Note - order isn't retained. Python doesn't care about order.
for key, value in glossary.items():
    print(key + ": " + value)

# What if we want to iterate through the keys?
for term in glossary:
    print("The key is: " + term)
# Can also explicitely use .keys()
for term in glossary.keys():
    print("The key is: " + term)
# Hmmmm, how about values?
for definition in glossary.values():
    print("The value is: " + definition)