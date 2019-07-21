
def create_car(make, model, **car_attrs):
    car = {'make':make, 'model':model}
    for key, attribute in car_attrs.items():
        car[key] = attribute
    return car

car = create_car('Tesla', 'Model 3',
    range='long',
    drive='2wd')

print(car)