from enum import Enum


class AccountType(Enum):
    CURRENT = 1
    SAVINGS = 2
    CORPORATE = 3

    def __str__(self):
        return f"""
                    CURRENT = {self.CURRENT},
                    SAVINGS = {self.SAVINGS},
                    CORPORATE = {self.CORPORATE}
                """

    def __repr__(self):
        return f"""
                    CURRENT = {self.CURRENT},
                    SAVINGS = {self.SAVINGS},
                    CORPORATE = {self.CORPORATE}
                """
