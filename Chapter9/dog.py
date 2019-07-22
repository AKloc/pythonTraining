# Finally - classes!

# In python, caps mean classes. Once again, indentation matters.
# self is always the first parameter so that the method can work on itself.
# For earlier Python versions, this next line would have to be:
#   class Dog(object):
class Dog():

    # Here's our constructor. "self" always comes first.
    # name and age are public.
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


# Let's use the class.
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name + ".")
print("My dog's age is " + str(my_dog.age) + ".")
my_dog.roll_over()
my_dog.sit()
print("\n")
your_dog = Dog('lucy', 3)
print("Your dog's name is " + your_dog.name + ".")
print("Your dog's age is " + str(your_dog.age) + ".")
your_dog.roll_over()
your_dog.sit()