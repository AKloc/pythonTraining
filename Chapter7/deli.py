sandwich_orders = ['ham', 'pastrami', 'capicola', 'pastrami', 'turkey', 'pbj', 'pastrami']
finished_sandwiches = []

# while len(sandwich_orders) > 0:
#     sandwich = sandwich_orders.pop()
#     finished_sandwiches.append(sandwich)

# print("Sandwich orders: " + str(sandwich_orders))
# print("Finised sandwiches: " + str(finished_sandwiches))

print("Let's get rid of the pastrami.")
while len(sandwich_orders) > 0:
    sandwich = sandwich_orders.pop()
    if sandwich != 'pastrami':
        finished_sandwiches.append(sandwich)

print("Sandwich orders: " + str(sandwich_orders))
print("Finised sandwiches: " + str(finished_sandwiches))