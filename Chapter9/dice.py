from random import randint

class Die():
    def __init__(self, sides=6):
        self.num_sides = sides
    
    def roll_die(self):
        print("Random #: " + str(randint(1, self.num_sides)))

# Remember, don't have to instantiate a class with "new" in Python.
six_sides = Die(6)
six_sides.roll_die()

two_sides = Die(2)
two_sides.roll_die()