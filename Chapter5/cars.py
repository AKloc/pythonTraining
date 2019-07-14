# if statements are as expected. Don't forget the colon.
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# re-writing this to get the same output...
print('Different logic, same result:')
for car in cars:
    if car != 'bmw':
        print(car.title())
    else:
        print(car.upper())

# and / or operators...
ages = [21, 18, 19, 30, 40, 65]
print("What ages are old enough to drink and not too old to go to clubs?")
for age in ages:
    if age >= 21 and age <= 40:
        print(age)

# elseif isn't a thing, but elif is.
for age in ages:
    print("Looking at age " + str(age))
    if age == 21:
        print("You can JUST imbibe.")
    elif age <= 18:
        print("You're too little.")
    elif age == 19:
        print("You can go crazy in Canada.")
    else:
        print("You can do whatever you want.")