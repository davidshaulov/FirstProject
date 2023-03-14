from ILS import ILS
from USD import USD
list = []

"""------this function is checking if the value to convert is number or not------"""


def check_amount():

    try:
        value_to_convert = float(input('please enter an amount to convert - '))
        return value_to_convert
    except ValueError:
        return "invalid value"


"""------this function is checking if the user wants to make another conversion------"""


def more_conversion():
    while True:
        another_conversion = input("Would you like to make another conversion? (Y/N)-  ")
        if another_conversion == "Y" or another_conversion == "y":
            get_user_value()
            break
        elif another_conversion == "N" or another_conversion == "n":
            print("These are the conversions you made:\n","-" * 34)
            print(list)
            print("Thanks for using our currency converter.\n","-" * 39)
            result_file = open("C:/results.txt", 'r+')
            result_file.write(str(list))
            break
        else:
            continue


"""------this function gets the conversion choice and make the convert------"""

def get_user_value():
    welcome_flag = 1
    if welcome_flag == 1:
        print("Welcome to currency converter")
        print("-" * 30)
        print("Please choose an option (1/2): ")
        print("-" * 30)
        choice_input = input("1. Dollars to Shekel \n2. Shekel to Dollars\n  --> ")
    else:
        choice_input = input("1. Dollars to Shekel \n2. Shekel to Dollars\n  --> ")
    while True:
        if choice_input == '1':
            amount_input = check_amount()
            if amount_input == "invalid value":
                print("your input wasn't a number let's try again")
                print("-" * 42)
            else:
                shekel = ILS()
                result = shekel.calculate(amount_input)
                list.append(result)
                more_conversion()
                welcome_flag += 1
                break
        elif choice_input == '2':
            amount_input = check_amount()
            if amount_input == "invalid value":
                print("your input wasn't a number let's try again")
                print("-" * 42)
            else:
                dollar = USD()
                result = dollar.calculate(amount_input)
                list.append(result)
                more_conversion()
                welcome_flag += 1
                break
        else:
            print("invalid choice, please try again")
            print("-"*32)
            choice_input = input("1. Dollars to Shekel \n2. Shekel to Dollars\n  --> ")


def main():

    get_user_value()


main()
