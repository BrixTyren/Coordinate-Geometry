
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


# two decimal format function
def decimal(x):
    return "{:.2f}".format(x)


# Main Routine

# Get inputs and calculate midpoint
x1 = num_check("Enter Point (x1): ", "Please enter a valid integer",
               float)
y1 = num_check("Enter Point (y1): ", "Please enter a valid integer",
               float)
x2 = num_check("Enter Point (x2): ", "Please enter a valid integer",
               float)
y2 = num_check("Enter Point (y2): ", "Please enter a valid integer",
               float)

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


gradient_print = f"Gradient = {gradient_formatted}"
print(gradient_print)
