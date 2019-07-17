favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

# Don't forget about this trick. We can iterate through the key
#   and values at the same time by using .items().
for name, languages in favorite_languages.items():
    print(name + "'s favorite languages are: ")
    for language in languages:
        print(language)