def check_amount():
    try:
        value_to_convert = float(input('please enter an amount to convert - '))
        return value_to_convert
    except ValueError:
        return False


def get_user_value():
    print("Welcome to currency converter \nPlease choose an option (1/2): ")
    choice_input = input("1. Dollars to Shekel \n2. Shekel to Dollars\n")
    while True:
        if choice_input == '1':

            if not check_amount():
                print("your input wasn't a number let's try again")
                break
            else:
                value_to_convert = check_amount()
                shekel = ILS()
                shekel.calculate(value_to_convert)

        elif choice_input == '2':

            if not check_amount():
                print("your input wasn't a number let's try again")
                break
            else:
                value_to_convert = check_amount()
                dollar = USD()
                dollar.calculate(value_to_convert)

        else:
            choice_input = input("invalid choice, please try again\n1. Dollars to Shekel \n2. Shekel to Dollars\n")

    get_user_value()


get_user_value()
