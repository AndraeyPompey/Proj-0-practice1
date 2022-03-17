from abc import ABC, abstractmethod

from entities.account_class2 import Account2


class Account2DaoInterface(ABC):

    @abstractmethod
    def create_account(self, account2: Account2)->Account2:
        pass

    @abstractmethod
    def get_account_by_account_id(self, account2_id: int)-> Account2:
        pass

    @abstractmethod
    def get_all_accounts_by_customer_id(self, customer_id: int)-> list[Account2]:
        pass

    @abstractmethod
    def update_account_by_account_id(self, account: Account2)-> Account2:
        pass

    @abstractmethod
    def transfer(self, sender_id: int, receiver_id: int, amount: float)-> bool:
        pass

    @abstractmethod
    def delete_account_by_id(self, account2_id: int)-> bool:
        pass

    # @abstractmethod
    # def delete_all_accounts_by_customer_id(self, customer_id: int)->bool:
    #     pass