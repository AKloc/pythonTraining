# This is neat. Don't have to define anything in terms of void or string
#   for a return type, you just return something or you don't.
# def get_formateed_name(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name.title()


# print(get_formateed_name('andy', 'kloc'))



# Optional parameters. This is weirder and feels more like a hack that uses default 
#   parameters. Set it to '' and check value.
def get_formateed_name(first_name, last_name, middle_name = ''):
    if middle_name:        
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = "No middle name."
    return full_name.title()


print(get_formateed_name('andy', 'kloc'))