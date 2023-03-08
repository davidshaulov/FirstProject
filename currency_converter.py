class ILS:

    def __init__(self, value):
        self.value = value

    @staticmethod
    def get_value():
        return 0.28

    def calculate(self, choice_input):
        return choice_input * self.get_value()


class USD:

    def __init__(self, value):
        self.value = value

    @staticmethod
    def get_value():
        return 3.52

    def calculate(self, choice_input):
        return choice_input * self.get_value()


def get_user_value():
    print("Welcome to currency converter \nPlease choose an option (1/2): ")
    choice_input = input("1. Dollars to Shekel \n2. Shekel to Dollars\n")

    while True:
        if choice_input == '1':
            value_to_convert = float(input('please enter an amount to convert'))
            print("good")
            shekel = ILS()
        elif choice_input == '2':
            value_to_convert = float(input('please enter an amount to convert'))
            print("good")
            dollar = USD()
        else:
            choice_input = input("invalid choice, please try again\n1. Dollars to Shekel \n2. Shekel to Dollars\n")


if __name__ == '__main__':







