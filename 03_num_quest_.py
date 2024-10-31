# === Functions go here ===

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

# Ask user how many questions they will be answering
for item in range(0, 6):
    number_of_questions = num_check("How many questions will you be answering? ",
                                    "Please enter an integer...\n", int)

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
        print(f"You chose {number_of_questions} question/s...\n")
