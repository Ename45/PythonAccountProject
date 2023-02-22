from enum import Enum


class State(Enum):
    ABIA = 1
    AKWAIBOM = 2
    EKITI = 3
    LAGOS = 4
    ABUJA = 5
    EDO = 6
    BENUE = 7
    KADUNA = 8

    def __str__(self):
        return f"""
              ABIA = {self.ABIA},
              AKWAIBOM = {self.AKWAIBOM},
              EKITI = {self.EKITI},
              LAGOS = {self.LAGOS},
              ABUJA = {self.ABUJA},
              EDO = {self.EDO},
              BENUE = {self.BENUE},
              KADUNA = {self.KADUNA}
          """

    def __repr__(self):
        return f"""
              ABIA = {self.ABIA},
              AKWAIBOM = {self.AKWAIBOM},
              EKITI = {self.EKITI},
              LAGOS = {self.LAGOS},
              ABUJA = {self.ABUJA},
              EDO = {self.EDO},
              BENUE = {self.BENUE},
              KADUNA = {self.KADUNA}
                  """
