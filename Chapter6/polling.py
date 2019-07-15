# Fun fact: this would be valid JSON if it used double quotes.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

people_who_should_poll = ['jen', 'mike', 'edward', 'bobby']

for person in people_who_should_poll:
    if person in favorite_languages.keys():
        print("Thanks for responding, " + person + ".")
    else:
        print("Plz respond, " + person + ". :(")
