motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

motorcycles[-2] = 'ducati'
# print(motorcycles)

# Starting with an empty list...
motorcycles = []
print(motorcycles)

motorcycles.append('honda')
motorcycles.append('yahama')
motorcycles.append('suzuki')
print(motorcycles)

print ("Deleting first element...")
del motorcycles[0]
print(motorcycles)

# Lists support pop, which hits the end of the list.
popped_motorcycle = motorcycles.pop()
motorcycle_string = str(motorcycles)
print("Popped motorcycle = " + popped_motorcycle + ". List = " + motorcycle_string)

# Add more elements and then remove by value.
motorcycles.append('suzuki')
motorcycles.append('honda')
print(motorcycles)
# Now let's remove suzuki, which is in the middle of the list.
motorcycles.remove('suzuki')
print(motorcycles)
# For kicks, let's try removing it again. Exception thrown.
# motorcycles.remove('suzuki')

# NOTE: remove() only removes the first occurence of the item in the list.

# Let's see an index of out range exception
motorcycles = []
# print(motorcycles[0])