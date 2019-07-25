# Playing with inheritance. Inherit from the car.

import car

class ElectricCar(car.Car):
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        # Electric cars have batteries.
        self.battery = Battery()

    # Overriding the method in car.py
    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about how many miles each battery size gets."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        print("This car can go approximately " + str(range) + " miles.")
    
    def upgrade_battery(self):
        if self.battery_size == 70:
            self.battery_size = 85

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()