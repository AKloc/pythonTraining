responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    name = input("\nWhat's your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in a dictionary.
    responses[name] = response

    response = input("Anyone else want to take the poll? ")
    if response == 'no':
        polling_active = False

# Show the results.
print("::::::POLL RESULTS::::::")
for name, response in responses.items():
    print(name + " voted for " + response)
