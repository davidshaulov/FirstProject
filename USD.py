class USD:

    @staticmethod
    def get_value():
        return 3.52

    def calculate(self, value_to_convert):
        print(value_to_convert * self.get_value())
