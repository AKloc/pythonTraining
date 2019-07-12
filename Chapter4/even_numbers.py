# What if we only want even numbers?
# This reads as "Start at 2, end at 11, and skip every two." -> [2, 4, 6, 8, 10]
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Start at 2, stop at 15, and count by 3s. -> [2, 5, 8, 11, 14]
print(str(list(range(2, 15, 3))))