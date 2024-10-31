# import library
import pandas


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

# Coordinate points entered in a list
points_list = []

# Small dta frame for testing
variable_dict = {
    "Points": points_list,
}

# Ask user how many questions they will be answering
while True:
    number_of_questions = num_check("How many questions will you be answering? ",
                                    "Please enter a valid number...\n", int)

    if number_of_questions <= 0:
        print("Please enter a number more than 0...\n")
    else:
        break

print(f"You chose {number_of_questions} questions...")

for i in range(number_of_questions):
    print(f"\nEnter coordinates for point set {i + 1}")

    # Get inputs from user
    x1 = num_check("Enter Point (x1): ", "Please enter a valid number", float)
    y1 = num_check("Enter Point (y1): ", "Please enter a valid number", float)
    x2 = num_check("Enter Point (x2): ", "Please enter a valid number", float)
    y2 = num_check("Enter Point (y2): ", "Please enter a valid number", float)

    # Append data to list
    points_list.append(f"({x1}, {y1}), ({x2}, {y2})")

    # # Print out points to check if it is correct (testing purpose only)
    # inside_list = f"(x1, y1), (x2, y2) = ({x1}, {y1}), ({x2}, {y2})"
    # print(inside_list)

# print out data frame to check if it is correct (testing purposes)
coordinate_frame = pandas.DataFrame(variable_dict)

print(coordinate_frame)
