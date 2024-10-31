
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
if (x2 - x1) and (y2 - y1) != 0:
    gradient = (y2 - y1) / (x2 - x1)
else:
    gradient = None

gradient_print = "Gradient = {:.2f}".format(gradient)
print(gradient_print)
