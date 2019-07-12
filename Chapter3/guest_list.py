guest_list = ['Freddie', 'David', 'Jesus']
invitation = ", consider yourself invited to dinner! Lucky you."

print(guest_list[0] + invitation)
print(guest_list[1] + invitation)
print(guest_list[2] + invitation)

# David can't make it. Remove him from the list.
missing_guest = 'David'
print("Shoot, " + missing_guest + " can't make it. Remove him from the list.")
guest_list.remove(missing_guest)
print("New guest list is " + str(len(guest_list)) + " members long. List:")
print(guest_list[0] + invitation)
print(guest_list[1] + invitation)

# Now I can invite three more people!
print("Now I can invite more people!")
guest_list.insert(0, 'Gilmour')
guest_list.insert(2, 'Clint')
guest_list.append('Jimi')
print(guest_list[0] + invitation)
print(guest_list[1] + invitation)
print(guest_list[2] + invitation)
print(guest_list[3] + invitation)
print(guest_list[4] + invitation)

# Whoops, smaller table.
print("The plot thickens... I have a smaller table. I'm a pretty horrible host.")
print("Sorry, " + guest_list.pop() + ", you can't go anymore.")
print("Sorry, " + guest_list.pop() + ", you can't go anymore.")
print("Sorry, " + guest_list.pop() + ", you can't go anymore.")
print("The guest list is now " + str(len(guest_list)) + " members long.")

print("Congrats, " + guest_list[0] + ", you're in.")
print("Congrats, " + guest_list[1] + ", you're in.")
# del guest_list[0 : 2]
del guest_list[0]
del guest_list[0]

print(guest_list)