cars = ['bmw', 'audi', 'toyota', 'subaru']

# This will sort alphabetically
cars.sort()
print(cars)

# This is interesting. Explicitly set the "reverse" parameter to True,
# which is case sensitive.
cars.sort(reverse = True)
print(cars)

# The sorted method doesn't change the list itself, but does a return
# a sorted version of it. NOTE: it wraps the list, as opposed to .sort.
sorted = sorted(cars)
print("Original list: " + str(cars))
print("Result of sorted() call: " + str(sorted))

# Let's play with .reverse()
print("Original list again: " + str(cars))
cars.reverse()
print("Original list after .reverse(): " + str(cars))

# How about len?
print("The length of the cars list is " + str(len(cars)))