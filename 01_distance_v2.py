# import libraries
import math


# === Functions go here ===

# number checker (not final)
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))
            return response

        except ValueError:
            print(error)


# === Main Routine ===
while True:
    # Define the coordinates of the first point (p1) and second point (p2) as a list.
    p1 = []
    p2 = []

    # Get user input and add it in the list to calculate
    point_one = num_check("Enter Point (x1): ", "Please enter a valid integer",
                          float)
    point_two = num_check("Enter Point (y1): ", "Please enter a valid integer",
                          float)
    point_three = num_check("Enter Point (x2): ", "Please enter a valid integer",
                            float)
    point_four = num_check("Enter point (y2): ", "Please enter a valid number",
                           float)

    p1.append(point_one)
    p1.append(point_two)
    p2.append(point_three)
    p2.append(point_four)

    print()
    # Calculate the distance between the two points using the distance formula.
    distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))

    # Print the calculated distance.
    print("Distance: {:.4f}".format(distance))
    print()
