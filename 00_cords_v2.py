# Import Libraries
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

        print("Please enter either 'yes' or 'no'...")


# number checker (mostly for floats)
def num_check(question, error, num_type):
    valid = False
    while not valid:
        try:
            response = num_type(input(question))
            return response

        except ValueError:
            print(error)


# two decimal format function
def decimal(x):
    return "{:.2f}".format(x)


# show instructions
def show_instructions():

    print('''
==== Instructions =====

This program will ask you for...
- How many questions you will be answering
- The coordinate points for each question (x1, y1)(x2, y2)

It will then use the coordinate points you entered
to produce an itemized list of the calculations 
for the line's distance, midpoint, and gradient on 
each set of question.

Please note that the number of questions you
entered is the number of times the program
will run. The program does not have an exit code
meaning you need to finish the program before
you can use it again.  

==== Program launched! =====''')


# Main Routine

print("==== Welcome to the Co-ordinate Geometry Calculator ====")

# Ask user if they want to see the instructions
want_instructions = yes_no("\nDo you want to read the instructions? ")

if want_instructions == "yes":
    show_instructions()
else:
    print("\n===== Program Launched! =====")

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

# Ask user how many questions they will be answering (check for typos)
while True:
    number_of_questions = num_check("\nHow many questions will you be answering? ",
                                    "Please enter a valid number...\n", int)

    if number_of_questions <= 0:
        print("Please enter a number more than 0...\n")

    # typo checker / confirmation (the program does not have an exit code)
    elif number_of_questions > 10:
        typo_check = yes_no(f"Are you sure you want to answer {number_of_questions}"
                            f" questions? ")

        if typo_check == "no":
            continue

        else:
            break

    else:
        print(f"You chose {number_of_questions} question/s...")
        break

# Loop according to number of questions entered w/ heading for each set
for i in range(number_of_questions):
    print(f"\n=== Enter coordinates for point set {i + 1} ===")

    # Get coordinate points from user
    x1 = num_check("Enter Point (x1): ", "Please enter a valid number...", float)
    y1 = num_check("Enter Point (y1): ", "Please enter a valid number...", float)
    x2 = num_check("Enter Point (x2): ", "Please enter a valid number...", float)
    y2 = num_check("Enter Point (y2): ", "Please enter a valid number...", float)

    # Calculate the distance between the two points using the distance formula.
    distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))
    # Round to 2dp
    distance_formatted = decimal(distance)

    # Calculate the midpoint between two points
    first_mid_point = (x1 + x2) / 2
    second_mid_point = (y1 + y2) / 2
    midpoint = (first_mid_point, second_mid_point)

    # Calculate the gradient using 2 points
    # Check for vertical or horizontal line...
    if (x2 - x1) != 0:
        gradient = (y2 - y1) / (x2 - x1)
        # Round to 2dp
        gradient_formatted = decimal(gradient)

        # check if gradient is exactly 0 to avoid displaying "-0"
        # it also avoids having decimal places on 0 --> "0.00"
        if gradient == 0:
            gradient_formatted = "0"

    else:
        gradient_formatted = "undefined-vertical line"

    # Append data to lists
    points_list.append(f"({x1}, {y1}), ({x2}, {y2})")
    distance_list.append(distance_formatted)
    midpoint_list.append(midpoint)
    gradient_list.append(gradient_formatted)

# Coordinate Frame Heading
print("\n==== Coordinate Points ====")

coordinate_frame = pandas.DataFrame(variable_dict)
coordinate_frame = coordinate_frame.set_index('Points')

# Print DataFrame
print(coordinate_frame)
