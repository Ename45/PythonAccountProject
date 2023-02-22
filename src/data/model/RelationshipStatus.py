from enum import Enum


class RelationshipStatus (Enum):
    SINGLE = 1
    IN_A_RELATIONSHIP = 2
    ENGAGED = 3
    MARRIED = 4
    SEPERATED = 5
    DIVORCED = 6

    def __str__(self):
        return f"""
                SINGLE = {self.SINGLE},
                IN_A_RELATIONSHIP = {self.IN_A_RELATIONSHIP},
                ENGAGED = {self.ENGAGED},
                MARRIED = {self.MARRIED},
                SEPERATED = {self.SEPERATED}
                DIVORCED = {self.DIVORCED},
            """

    def __repr__(self):
        return f"""
                        SINGLE = {self.SINGLE},
                        IN_A_RELATIONSHIP = {self.IN_A_RELATIONSHIP},
                        ENGAGED = {self.ENGAGED},
                        MARRIED = {self.MARRIED},
                        SEPERATED = {self.SEPERATED}
                        DIVORCED = {self.DIVORCED},
                    """
