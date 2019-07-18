# Like C#, defaulted parameters come after non-defaults.
def describe_pet(pet_name, animal_type='cat'):
    print("\nI have a " + animal_type + ".")
    print("Its name is " + pet_name.title() + ".")

describe_pet('Hamster', 'Harry')
describe_pet('dog', 'willie')


# Let's use keyword arguments this time.
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='willie', animal_type='dog')
describe_pet(pet_name='coco')