# favorite_numbers = {
#     'shannon': 7,
#     'andy': 23,
#     'alex': 5,
#     'taylor': 10,
#     'asher': 1
# }

# print(favorite_numbers)


# Exercise 6-10 version that allows multiple favorite numbers
favorite_numbers = {
    'shannon': [7, 11],
    'andy': [23, 46],
    'alex': [5, 0],
    'taylor': [10, 100],
    'asher': [1]
}

for name, numbers in favorite_numbers.items():
    print(name + "'s favorite numbers are: " + str(numbers))