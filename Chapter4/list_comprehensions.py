# LIST COMPREHENSIONS
# We can express the squares.py code in just one line.

# squares = []
# for value in range(1,11):
#     squares.append(value ** 2)

# Basically... [do this to the value FOR EACH VALUE in whatever].
# Note, no colon.
squares = [value**2 for value in range(1,11)]
#print(squares)

# Neat. Lets you apply the same operation against the entire list.
adding_3 = [value + 3 for value in range(1, 6)]
print(adding_3)