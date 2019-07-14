# Tuples are just immutable lists. Use parens instead of brackets.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Can't do the below. Throws a tuple error "object does not support item assignment."
# dimensions[0] = 250

# You can loop over tuple values just like lists.
for dimension in dimensions:
    print(dimension)

# You can't MODIFY a tuple, but you can assign a new value to a variable that holds one.
dimensions = (400, 100)
print("After assigning a new tuple to dimensions...")
for dimension in dimensions:
    print(dimension)