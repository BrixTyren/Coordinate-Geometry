import pandas
import math


# Functions

# Checks that user has entered yes / no to a question
def yes_no(question):
    to_check = ["yes", "no"]

    valid = False
    while not valid:
        response = input(question).lower()
        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no...")


# checks that input is either a float or an
# integer that is more than zero. Takes in custom error message
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# show instructions
def show_instructions():
    print("\ninstructions go here\n")


# Main Routine

print("==== Welcome to the Co-ordinate Geometry Calculator ====\n")

# ask for instructions
want_instructions = yes_no("\nDo you want to read the instructions? ")

if want_instructions == "yes":
    show_instructions()
else:
    print("\n=== Program Launched! ===")

# Set up dictionaries and lists
points_list = []
distance_list = []
midpoint_list = []
gradient_list = []

# Create DataFrame
variable_dict = {
    "Points": points_list,
    "Distance": distance_list,
    "Midpoint": midpoint_list,
    "Gradient": gradient_list
}

# Get inputs and calculate midpoint and distance
x1 = num_check("Enter Point (x1): ", "Please enter a valid integer", float)
y1 = num_check("Enter Point (y1): ", "Please enter a valid integer", float)
x2 = num_check("Enter Point (x2): ", "Please enter a valid integer", float)
y2 = num_check("Enter Point (y2): ", "Please enter a valid integer", float)

# Calculate the distance between the two points using the distance formula.
distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

# Calculate the midpoint between two points
first_point = (x1 + x2) / 2
second_point = (y1 + y2) / 2
midpoint = (first_point, second_point)

# Calculate the gradient between 2 points
gradient = (y2 - y1) / (x2 - x1)

# Append data to lists
points_list.append(f"({x1}, {y1}), ({x2}, {y2})")
distance_list.append(distance)
midpoint_list.append(midpoint)
gradient_list.append(gradient)

coordinate_frame = pandas.DataFrame(variable_dict)
coordinate_frame = coordinate_frame.set_index('Points')

# Print DataFrame
print(coordinate_frame)
