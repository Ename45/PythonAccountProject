from typing import Type

from data.model.Address import Address
from data.model.Personal_information import PersonalInformation
from data.model.RelationshipToNextOfkin import RelationshipToNextOfKin


class NextOfKin:
    def __init__(self):
        self._next_of_kin_address = Address()
        self._next_of_kin_relationship = RelationshipToNextOfKin
        self._next_of_kin_personal_info = PersonalInformation()

    def set_next_of_kin_address(self, next_of_kin_address) -> None:
        self._next_of_kin_address = next_of_kin_address

    def get_next_of_kin_address(self):
        return self._next_of_kin_address

    def set_next_of_kin_relationship(self, next_of_kin_relationship) -> None:
        self._next_of_kin_relationship = next_of_kin_relationship

    def get_next_of_kin_relationship(self) -> Type[RelationshipToNextOfKin]:
        return self._next_of_kin_relationship

    def set_next_of_kin_personal_info(self, next_of_kin_personal_info) -> None:
        self._next_of_kin_personal_info = next_of_kin_personal_info

    def get_next_of_kin_personal_info(self):
        return self._next_of_kin_personal_info

    def __str__(self):
        return f"""
            Next Of Kin Address: {self._next_of_kin_address},
            Next Of Kin Relationship: {self._next_of_kin_relationship},
            Next Of Kin Personal Information: {self._next_of_kin_personal_info}
        """

    def __repr__(self):
        return f"""
            Next Of Kin Address: {self._next_of_kin_address},
            Next Of Kin Relationship: {self._next_of_kin_relationship},
            Next Of Kin Personal Information: {self._next_of_kin_personal_info}
               """
