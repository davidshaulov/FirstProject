"""
this function make calculate between the
input and the shekel exchange rate
"""


class ILS:

    @staticmethod
    def get_value():
        return 0.28

    def calculate(self, value_to_convert):
        result = value_to_convert * self.get_value()
        print(result)
        return result
