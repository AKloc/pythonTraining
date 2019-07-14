user_names = ['Ed', 'Tom', 'Gary', 'Andy', 'Eric', 'admin']

if not user_names:
    print("We don't have any users. Looks like no one is logging in.")
else:
    for user in user_names:
        if user == 'admin':
            print("Whoa, we've got an admin here.")
        else:
            print("You are now logged in, " + user + ".")