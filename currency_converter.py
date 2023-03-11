from ILS import ILS
from USD import USD


def check_amount():

    try:
        value_to_convert = float(input('please enter an amount to convert - '))
        return value_to_convert
    except ValueError:
        return "invalid value"


def get_user_value():

    print("Welcome to currency converter \nPlease choose an option (1/2): ")
    choice_input = input("1. Dollars to Shekel \n2. Shekel to Dollars\n")
    while True:
        list = []
        if choice_input == '1':
            if check_amount() == "invalid value":
                print("your input wasn't a number let's try again")
                break
            else:
                shekel = ILS()
                shekel.calculate(check_amount())
                list.append(result)
                print(list)
                break

        elif choice_input == '2':
            if check_amount() == "invalid value":
                print("your input wasn't a number let's try again")
                break
            else:
                dollar = USD()
                dollar.calculate(check_amount())
                list.append(result)
                print(list)
                break
        else:
            choice_input = input("invalid choice, please try again\n1. Dollars to Shekel \n2. Shekel to Dollars\n")

    get_user_value()


def main():

    get_user_value()


main()
