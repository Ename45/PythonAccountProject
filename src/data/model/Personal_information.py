from typing import Type

from data.model.Country import Country
from data.model.Gender import Gender
from data.model.RelationshipStatus import RelationshipStatus


class PersonalInformation:
    def __init__(self):
        self._person_id: int = 0
        self._first_name: str = ""
        self._last_name: str = ""
        self._gender = Gender
        self._relationship_status = RelationshipStatus
        self._mobile_number: str = ""
        self._age: str = ""
        self._country_code = Country
        self._local_government: str = ""
        self._state_of_origin: str = ""
        self._email_address: str = ""

    def set_person_id(self, person_id):
        self._person_id = person_id

    def get_person_id(self):
        return self._person_id

    def set_full_name(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_full_name(self):
        return '{} {}'.format(self._first_name, self._last_name)

    def set_first_name(self, first_name) -> None:
        self._first_name = first_name

    def get_first_name(self) -> str:
        return self._first_name

    def set_last_name(self, last_name) -> None:
        self._last_name = last_name

    def get_last_name(self) -> str:
        return self._last_name

    def set_mobile_number(self, number: str) -> None:
        self._mobile_number = number

    def get_mobile_number(self) -> str:
        return self._mobile_number

    def set_age(self, age: str) -> None:
        self._age = age

    def get_age(self) -> str:
        return self._age

    def set_country_code(self, country_code) -> None:
        self._country_code = country_code

    def get_country_code(self) -> Type[Country]:
        return self._country_code

    def set_gender(self, gender: str) -> None:
        self._gender = gender

    def get_gender(self) -> Type[Gender]:
        return self._gender

    def set_relationship_status(self, relationship_status: str) -> None:
        self._relationship_status = relationship_status

    def get_relationship_status(self) -> Type[RelationshipStatus]:
        return self._relationship_status

    def set_local_govt(self, lga: str) -> None:
        self._local_government = lga

    def get_local_govt(self) -> str:
        return self._local_government

    def set_state_of_origin(self, state: str) -> None:
        self._state_of_origin = state

    def get_state_of_origin(self) -> str:
        return self._state_of_origin

    def set_email_address(self, email: str) -> None:
        self._email_address = email

    def get_email_address(self) -> str:
        return self._email_address

    def __repr__(self):
        return f"""
                    person_id: {self._person_id},
                    first_name: {self._first_name},
                    last_name: {self._last_name},
                    Gender: {self._gender},
                    Relationship Status: {self._relationship_status},
                    Mobile Number: {self._mobile_number},
                    country: {self._country_code},
                    Local Government Area: {self._local_government},
                    State of Origin: {self._state_of_origin},
                    Email Address: {self._email_address}
                """

    def __str__(self):
        return f"""
            person_id: {self._person_id},
            first_name: {self._first_name},
            last_name: {self._last_name},
            Gender: {self._gender},
            Relationship Status: {self._relationship_status},
            Mobile Number: {self._mobile_number},
            country: {self._country_code},
            Local Government Area: {self._local_government},
            State of Origin: {self._state_of_origin},
            Email Address: {self._email_address}
        """

# if __name__ == '__main__':
#     per = PersonalInformation()
#     country = Country
#     per.set_country_code(country.FINLAND.value)
#     print(per.get_country_code())
