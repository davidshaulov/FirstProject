"""
this function make calculate between the
input and the dollar exchange rate
"""


class USD:

    @staticmethod
    def get_value():
        return 3.52

    def calculate(self, value_to_convert):
        result = value_to_convert * self.get_value()
        print("%.1f" % result)
        return result

