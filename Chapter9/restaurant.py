
# Don't forget the () at the end.
class Restaurant():
    # And don't forget the trailing __.
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name + 
            " and it serves " + self.cuisine_type + " cuisine.")
    
    def open_restaurant(self):
        print("The restaurant is open!")

# Don't need to use "new" here or anything.
# como = Restaurant("Como's", "Italian")
# como.describe_restaurant()
# como.open_restaurant()

# teso = Restaurant("Teso's", "Pizza")
# teso.describe_restaurant()

# ding_how = Restaurant("Ding How", "Chinese")
# ding_how.describe_restaurant()