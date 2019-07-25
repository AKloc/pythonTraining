class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

        # This assigns a default value.
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def set_odometer(self, mileage):
        if mileage <= self.odometer_reading:
            print("You can't roll back the mileage.")
        else:
            self.odometer_reading = mileage
    
    def fill_gas_tank(self):
        print("Filled the gas tank")


# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 9000
# my_new_car.set_odometer(8000)
# print("Odotmeter reading: " + str(my_new_car.odometer_reading))