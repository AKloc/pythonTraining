# Slicing apparently is the same as copying elements. So if we set a slice of [:] it copies the entire list.
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]


# Alright... what happens if we change falafel in my_foods? Does it change friend_foods? Nope.
my_foods[1] = 'fries'


# What if we add an element to friend_foods? Won't show up on my_foods.
friend_foods.append('ice cream')

print("After messing with the two sliced lists individually:")
print(my_foods)
print(str(friend_foods) + "\n")


# What if we just set my_foods = friend_foods? Then it points my_foods to the my_friends var.
# Changing one will change the other because they're pointing at the same thing now.
my_foods = friend_foods
my_foods[1] = 'taco'

print("After my_foods = friend_foods and changing falafel to taco on just my_foods:")
print(my_foods)
print(friend_foods)