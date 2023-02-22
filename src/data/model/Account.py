from typing import Type

from data.model.AccountType import AccountType
from data.model.Bank import Bank
from data.model.User import User


class Account(object):
    def __init__(self):
        self._account_id: int = 0
        self._pin = None
        self._card_number = None
        self._bank = Bank()
        self._account_type = AccountType
        self._account_number: str = ""
        self._account_name: str = ""
        self._account_user = User()
        self._transfer_limit = None
        self._account_limit = None

    def set_user(self, user):
        self._account_user = user

    def get_user(self):
        return self._account_user

    def set_id(self, account_id):
        self._account_id = account_id

    def get_id(self):
        return self._account_id

    def set_pin(self, pin) -> None:
        self._pin = pin

    def set_card_number(self, card_number) -> None:
        self._card_number = card_number

    def get_card_number(self):
        return self._card_number

    def set_account_number(self, acc_number: str) -> None:
        self._account_number = acc_number

    def get_account_number(self):
        return self._account_number

    def set_account_name(self, account_name: str) -> None:
        self._account_name = account_name

    def get_account_name(self):
        return self._account_name

    def set_account_user(self, acc_user) -> None:
        self._account_user = acc_user

    def get_account_user(self):
        return self._account_user

    def set_account_type(self, account_type) -> None:
        self._account_type = account_type

    def get_account_type(self) -> Type[AccountType]:
        return self._account_type

    def set_transfer_limit(self, limit_to_transfer):
        self._transfer_limit = limit_to_transfer

    def get_transfer_limit(self):
        return self._transfer_limit

    def set_account_limit(self, limit_on_acc):
        self._account_limit = limit_on_acc

    def get_account_limit(self):
        return self._account_limit

    def __str__(self):
        return f"""User Account Id: {self._account_id}"
        User Account Pin: {self._pin},
        User Card: {self._card_number},
        User Bank: {self._bank},
        User Account Type: {self._account_type},
        User Account Number: {self._account_number},
        User Account Name: {self._account_name},
        Account User: {self._account_user},
        User Transfer Limit: {self._transfer_limit},
        User Account Limit: {self._account_limit}        
        """

    def __repr__(self):
        return f"""User Account Id; {self._account_id}"
               User Account Pin: {self._pin},
               User Card: {self._card_number},
               User Bank: {self._bank},
               User Account Type: {self._account_type},
               User Account Number: {self._account_number},
               User Account Name: {self._account_name},
               Account User: {self._account_user},
               User Transfer Limit: {self._transfer_limit},
               User Account Limit: {self._account_limit}        
               """
