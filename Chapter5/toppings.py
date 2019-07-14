requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     print("Adding " +requested_topping + ".")

# print("\nFinished making your pizza!")

# What if the pizzeria ran out of peppers???
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we're out of green peppers right now.")
#     else:
#         print("Adding " +requested_topping + ".")

# print("\nFinished making your pizza!")


# What if we started with an empty list? We can check by looking at equality
#   on the list itself. True means it has something in it, False otherwise.
requested_toppings = []

if not requested_toppings:
    print("No toppings. Guessing you just want a plain cheese pizza.")
else:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("Sorry, we're out of green peppers right now.")
        else:
            print("Adding " +requested_topping + ".")

print("\nFinished making your pizza!")