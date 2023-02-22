from enum import Enum


class RelationshipToNextOfKin(Enum):
    FATHER = 1
    MOTHER = 2
    BROTHER = 3
    SISTER = 4
    SON = 5
    DAUGHTER = 6
    UNCLE = 7
    AUNTY = 8

    def __str__(self):
        return f"""
                    FATHER = {self.FATHER},
                    MOTHER = {self.MOTHER},
                    BROTHER = {self.BROTHER},
                    SISTER = {self.SISTER},
                    SON = {self.SON}
                    DAUGHTER = {self.DAUGHTER},
                    UNCLE = {self.UNCLE},
                    AUNTY = {self.AUNTY}
                """

    def __repr__(self):
        return f"""
                    FATHER = {self.FATHER},
                    MOTHER = {self.MOTHER},
                    BROTHER = {self.BROTHER},
                    SISTER = {self.SISTER},
                    SON = {self.SON}
                    DAUGHTER = {self.DAUGHTER},
                    UNCLE = {self.UNCLE},
                    AUNTY = {self.AUNTY}
                """
