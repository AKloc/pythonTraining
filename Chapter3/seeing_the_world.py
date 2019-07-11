places_to_visit = ['Paris', 'Greece', 'Barcelona', 'London', 'Egypt']
print("Original order: " + str(places_to_visit))

sorted_places = sorted(places_to_visit)
print("Sorted order: " + str(sorted_places))
print("Proof that the original is unmodified: " + str(places_to_visit))

places_to_visit.reverse()
print("After .reverse: " + str(places_to_visit))

places_to_visit.reverse()
print("After another .reverse to restore order: " + str(places_to_visit))

places_to_visit.sort()
print("After .sort(): " + str(places_to_visit))

places_to_visit.sort(reverse = True)
print("After .sort(reverse=True): " + str(places_to_visit))