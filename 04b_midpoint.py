
# functions

# number checker
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))
            return response

        except ValueError:
            print(error)


# Main Routine
for item in range(0, 6):
    # Get inputs and calculate midpoint for checking
    x1 = num_check("Enter Point (x1): ", "Please enter a valid integer",
                   float)
    y1 = num_check("Enter Point (y1): ", "Please enter a valid integer",
                   float)
    x2 = num_check("Enter Point (x2): ", "Please enter a valid integer",
                   float)
    y2 = num_check("Enter Point (y2): ", "Please enter a valid integer",
                   float)

    # Calculate the midpoint between 2 co-ordinate points
    first_point = (x1 + x2) / 2
    second_point = (y1 + y2) / 2

    print(f"Midpoint co-ordinate: ({first_point}, {second_point})\n")
