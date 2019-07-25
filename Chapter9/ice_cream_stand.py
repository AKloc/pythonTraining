import restaurant

# Don't need to use "def" when creating a class.
class IceCreamStand(restaurant.Restaurant):
    # Don't forget to use self in all of the method parameters
    def __init__(self, restaurant_name):
        # Use super()., not super.
        super().__init__(restaurant_name, "Ice Cream")
        self.flavors = ['vanilla', 'chocolate', 'twist']
    
    def print_flavors(self):
        for flavor in self.flavors:
            print(flavor)


ice_cream_stand = IceCreamStand("Berrafato's")
ice_cream_stand.describe_restaurant()
ice_cream_stand.print_flavors()