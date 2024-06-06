# import libraries


# **** Functions go here ****

# check that input is either a float or an
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