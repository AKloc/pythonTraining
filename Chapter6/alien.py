# Let's play with dictionaries. Curly braces.
alien_o = {'color':'green', 'points':5}
print(alien_o['color'])
print(alien_o['points'])

# Accessing the data.
new_points = alien_o['points']
print("You just earned " + str(new_points) + " points!")

# We can add additional key-value pairs to the dictionary after it's been created, too.
alien_o['x_position'] = 0
alien_o['y_position'] = 25
alien_o['color'] = 'blue'
print(alien_o)

# Using an empty dictionary is the same as a list.
alien_o = {}
alien_o['color'] = 'green'
alien_o['points'] = 5
print(alien_o)

# Modifying existing values works just like you'd think.
alien_o['color'] = 'red'
print(alien_o)

# Removing is also the same.
del alien_o['color']
print(alien_o)