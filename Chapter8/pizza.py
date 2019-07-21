# Note the *parameter. Tells Python to make an empty tuple called toppings
#   and fills it with however many parameters are sent. (Remember - only diff
#   between a tuple and a list is mutability. Also, tuples use parens instead
#   of square brackets). Like optional parameters, has to be at the end of list.
def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    print("You want a " + size + " pizza with " + str(toppings))

def another_method(message):
    print("You sent " + message)

def hello_world():
    print("Hello world.")

# make_pizza('large', 'pepperoni')
# make_pizza('party', 'mushrooms', 'green peppers', 'extra cheese')