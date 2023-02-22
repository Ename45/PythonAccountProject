from typing import Type

from data.model.Country import Country
from data.model.State import State


class Address:
    def __init__(self):
        self._address_id: int = 0
        self._street_number: int = 0
        self._street_name: str = ""
        self._postal_code: int = 0
        self._local_government: str = ""
        self._state = State
        self._country = Country

    def set_address_id(self, address_id):
        self._address_id = address_id

    def bank_id(self):
        return self._address_id

    def set_street_number(self, street_number: int) -> None:
        self._street_number = street_number

    def get_street_number(self):
        return self._street_number

    def set_street_name(self, street_name: str) -> None:
        self._street_name = street_name

    def get_street_name(self):
        return self._street_name

    def set_postal_code(self, postal_code: int) -> None:
        self._postal_code = postal_code

    def get_postal_code(self):
        return self._postal_code

    def set_local_government(self, lga: str) -> None:
        self._local_government = lga

    def get_local_government(self):
        return self._local_government

    def set_country(self, country) -> None:
        self._country = country

    def get_country(self) -> Type[Country]:
        return self._country

    def set_state(self, state) -> None:
        self._state = state

    def get_state(self) -> Type[State]:
        return self._state

    def __str__(self):
        return f"""
            Address Id: {self._address_id},
            Street Number: {self._street_number},
            Street Name: {self._street_name},
            Postal Code: {self._postal_code},
            Local Government: {self._local_government},
            Country: {self._country},
            State: {self._state}
        """

    def __repr__(self):
        return f"""
            Address Id: {self._address_id},
            Street Number: {self._street_number},
            Street Name: {self._street_name},
            Postal Code: {self._postal_code},
            Local Government: {self._local_government},
            Country: {self._country},
            State: {self._state}
               """
