# Modules! Just import the name of the python file, and then reference the 
#   module by doing module_name.function_name().
import pizza
# We can also pull in a specific method(s).
from pizza import make_pizza, another_method
# ... and we can rename them in the file we're using.
from pizza import hello_world as hw
# Finally, we can import every function by using *.
# from pizza import *


# Lower two use the indirect "import pizza" method.
pizza.make_pizza('large', 'pepperoni')
pizza.make_pizza('party', 'mushrooms', 'green peppers', 'extra cheese')

# This uses the more specific from pizza statement
another_method("Here's the message.")

# And this one uses our method alias.
hw()