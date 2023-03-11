class ILS:

    @staticmethod
    def get_value():
        return 0.28

    def calculate(self, value_to_convert):
        print(value_to_convert * self.get_value())
