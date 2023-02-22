from data.model.Address import Address
from data.model.Next_of_kin import NextOfKin
from data.model.Personal_information import PersonalInformation


class User:
    def __init__(self):
        self._next_of_kin = NextOfKin()
        self._user_address = Address()
        self._user_personal_information = PersonalInformation()

    def set_next_of_kin(self, next_of_kin):
        self._next_of_kin = next_of_kin

    def get_next_of_kin(self):
        return self._next_of_kin

    def set_user_address(self, user_address):
        self._user_address = user_address

    def get_user_address(self):
        return self._user_address

    def set_user_personal_information(self, user_personal_information):
        self._user_personal_information = user_personal_information

    def get_user_personal_information(self):
        return self._user_personal_information

    def __str__(self):
        return f"""
            Next Of Kin: {self._next_of_kin},
            User Address: {self._user_address},
            User Personal Information: {self._user_personal_information}
        """

    def __repr__(self):
        return f"""
            Next Of Kin: {self._next_of_kin},
            User Address: {self._user_address},
            User Personal Information: {self._user_personal_information}
               """
