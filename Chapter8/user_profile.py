# The ** lets us send whatever keyword arguments we want to into the function.
#   Sort of a weird one, but cool way to send in a lot of info without
#   overcrowding the signature. Would probably still rather pass in an object.
def build_profile(first, last, **user_info):
    """ Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Note that location and field aren't in quotes. Same syntax as keyword args
#   even though they aren't explicitely defined in the signature.
user_profile = build_profile('albert', 'einsten',
    location='princeton',
    field='physics')

my_profile = build_profile('Andy', 'K', 
    location='New York',
    num_of_kids=2,
    car='Model 3')

print(my_profile)