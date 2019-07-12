# range() has off-by-one behavior. This next line will start counting at 1
#  and will stop when hits the second value. So in this case, when it hits 5,
#  it stops processing.
for value in range(1,5):
    print(value)

# You can use list() to make a list from the range.
number_list = list(range(1,6))
print(number_list)