first_number = input("First number? ")
second_number = input("Second number? ")

try:
    first_int = int(first_number)
    second_int = int(second_number)
except ValueError:
    print("Couldn't parse one of the numbers.")
else:
    print(first_number + " + " + second_number + " = " + str(first_int + second_int))