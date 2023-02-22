from enum import Enum


class Gender(Enum):
    MALE = 1
    FEMALE = 2
    LGBTQ = 3

    def __str__(self):
        return f"""
                    MALE = {self.MALE},
                    FEMALE = {self.FEMALE},
                    LGBTQ = {self.LGBTQ}
                """

    def __repr__(self):
        return f"""
                    MALE = {self.MALE},
                    FEMALE = {self.FEMALE},
                    LGBTQ = {self.LGBTQ}
                        """
