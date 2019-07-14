# Taking slices of lists.
players = ['charles', 'martina', 'michael', 'florence', 'eli', 'herp', 'derp']
print(players[0:3]) # Note that this is a colon, not a comma.
# Leave the index out and it'll start at the beginning.
print(players [:3])
# Leave the ending out and it'll include everything from the index to the end of the list.
print(players [3:])
# How about getting the last two players? Use -2 as the index.
print(players[-2:])