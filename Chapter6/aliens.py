alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first five aliens.
# for alien in aliens[:5]:
#     print(alien)
# print("...")

print("Total length of aliens list = " + str(len(aliens)))

# Neat, but let's change some of the green aliens.
for alien in aliens[5:10]:
    alien['color'] = 'yellow'
    alien['points'] = 10
    alien['speed'] = 'medium'

for alien in aliens:
    print(alien)