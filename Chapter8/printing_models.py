# # Start with some designs that need to be printed.
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Simulate printing each design, until none are left.
# # Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     # Simulate creating a 3D print from the design.
#     print("Printing model: " + current_design)
#     completed_models.append(current_design)

# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)


# SO - parameters are based by REFERENCE. Changes to vars in the method stick.
# def print_models(unprinted_designs, completed_models):
#     """
#     Simulate printing each design, until none are left.
#     Move each design to completed_models after printing.
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         # Simulate creating a 3D print from the design.
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """Show all the models that were printed."""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

from printing_methods_imports import *

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# These will pass by reference, but if we use [:] it'd make a copy of the variables instead.
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print("Contents of unprinted_designs: " + str(unprinted_designs))
