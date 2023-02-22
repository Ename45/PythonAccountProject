from abc import ABC, abstractclassmethod, abstractmethod


class AccountRepositoryInterface(ABC):
    @abstractmethod
    def create_new_account(self, first_name, last_name, mobile_number, age, gender, relationship_status, lga, state, country,
                           email):
        pass

    @abstractmethod
    def deposit(self, amount, pin):
        pass

    @abstractmethod
    def withdraw(self, amount, pin):
        pass

    @abstractmethod
    def transfer(self, amount, account_name, account_number, bank_name, pin):
        pass

    @abstractmethod
    def check_balance(self, account_number, pin):
        pass
