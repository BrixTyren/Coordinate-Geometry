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

# Gets point inputs from user
while True:
    # print("=== Enter the value points below ===\n")
    point_one = num_check("Enter point (x1): ", "Please enter a valid number\n",
                          float)

    print("Point x1 -> {:.2f}\n".format(point_one))
