# === Functions go here ===

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


# === Main Routine ===

while True:
    print("Enter the value points below\n")
    point_one = num_check("Enter point (x1): ", "Please enter a valid number...",
                          int)
    point_two = num_check("Enter point (y1): ", "Please enter a valid number...",
                          int)

    print("Point x1 -> {}".format(point_one))
    print("Point y1 -> {}".format(point_two))
