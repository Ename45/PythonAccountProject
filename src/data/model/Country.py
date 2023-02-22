from enum import Enum


class Country(Enum):
    NIGERIA = "234"
    GHANA = "233"
    GERMANY = "49"
    GEORGIA = "995"
    SOUTH_AFRICA = "27"
    FRANCE = "33"
    FINLAND = "358"
    ITALY = "39"

    def __str__(self):
        return f"""
            NIGERIA = {self.NIGERIA},
            GHANA = {self.GHANA},
            GERMANY = {self.GERMANY},
            GEORGIA = {self.GEORGIA},
            SOUTH_AFRICA = {self.SOUTH_AFRICA},
            FRANCE = {self.FRANCE},
            FINLAND = {self.FINLAND},
            ITALY = {self.ITALY}
        """

    def __repr__(self):
        return f"""
                    NIGERIA = {self.NIGERIA},
                    GHANA = {self.GHANA},
                    GERMANY = {self.GERMANY},
                    GEORGIA = {self.GEORGIA},
                    SOUTH_AFRICA = {self.SOUTH_AFRICA},
                    FRANCE = {self.FRANCE},
                    FINLAND = {self.FINLAND},
                    ITALY = {self.ITALY}
                """
