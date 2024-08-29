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
    points_list = []

    # Get user input and add it in the list to calculate
    point_one = num_check("Enter Point (x1): ", "Please enter a valid integer",
                          float)
    point_two = num_check("Enter Point (y1): ", "Please enter a valid integer",
                          float)
    point_three = num_check("Enter Point (x2): ", "Please enter a valid integer",
                            float)
    point_four = num_check("Enter point (y2): ", "Please enter a valid number",
                           float)

    points_list.append(point_one)
    points_list.append(point_two)
    points_list.append(point_three)
    points_list.append(point_four)

    p1_list = "\n(x1, y1) = ({}, {})".format(points_list[0], points_list[1])
    p2_list = "(x2, y2) = ({}, {})".format(points_list[2], points_list[3])
    print(p1_list)
    print(p2_list)

    print()
    # Calculate the distance between the two points using the distance formula.
    distance = math.sqrt(((points_list[0] - points_list[2]) ** 2) +
                         ((points_list[1] - points_list[3]) ** 2))

    # Print the calculated distance.
    print("Distance: {:.2f}".format(distance))
    print()
