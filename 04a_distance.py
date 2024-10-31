# import libraries
import math


# === Functions go here ===

# === Main Routine ===

p1 = [2, 3]
p2 = [7, 10]

# Calculate the distance between the two points using the distance formula.
point_one = "(x1, y1) = ({}, {})".format(p1[0], p1[1])
point_two = "(x2, y2) = ({}, {})".format(p2[0], p2[1])
print(point_one)
print(point_two)

distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

# Print the calculated distance.
print("Distance: {:.2f}".format(distance))
