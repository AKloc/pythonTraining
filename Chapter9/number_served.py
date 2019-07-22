# Don't forget the () at the end.
class Restaurant():
    # And don't forget the trailing __.
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name + 
            " and it serves " + self.cuisine_type + " cuisine.")
    
    def open_restaurant(self):
        print("The restaurant is open!")

    def increment_number_served(self):
        self.number_served += 1

    def print_number_served(self):
        print(self.restaurant_name + "'s number of customers served is " + 
            str(self.number_served))

# Don't need to use "new" here or anything.
# como = Restaurant("Como's", "Italian")
# como.describe_restaurant()
# como.open_restaurant()

# teso = Restaurant("Teso's", "Pizza")
# teso.describe_restaurant()

# ding_how = Restaurant("Ding How", "Chinese")
# ding_how.describe_restaurant()

jims_steakout = Restaurant("Jim's Steakout", "American Fare")
jims_steakout.print_number_served()
jims_steakout.increment_number_served()
jims_steakout.print_number_served()