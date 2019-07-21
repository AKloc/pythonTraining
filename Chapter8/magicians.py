def show_magicians(magicians):
    print(magicians)

def make_great(magicians):
    # THE BELOW DOES NOT WORK because magician is just a copy.
    # for magician in magicians:
    #     magician = "The Great " + magician

    # THIS DOESN'T WORK EITHER, because using list comprehension creates a new
    #   list.
    # magicians = ["The great " + magician for magician in magicians]

    # This DOES work. From StackOverflow. This feels like a hack since we 
    #   haven't learned about enumerate() yet.
    # for i, magician in enumerate(magicians):
    #     magicians[i] = "The Great " + magician

    # This works, but feels revolting. Found online. Create a new list and then 
    #   use append to run over the original list's reference. I think this is
    #   what the book wants to roll with since it's in previous examples.
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        magician += " The Great"
        great_magicians.append(magician)
    
    while(great_magicians):
        magician = great_magicians.pop()
        magicians.append(magician)


magicians = ['magician_1', 'magician_2', 'magician_3']
make_great(magicians)
show_magicians(magicians)

# Call it again with a range. That will send a copy in and not affect the list.
magicians = ['magician_1', 'magician_2', 'magician_3']
make_great(magicians[:])
show_magicians(magicians)