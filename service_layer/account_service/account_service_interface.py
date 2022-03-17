from abc import ABC, abstractmethod

from data_access_layer.bank_dao.account_dao_interface import AccountDaoInterface
from entities.account_class2 import Account2


class AccountServiceInterface(ABC):

    def __init__(self, account_dao:AccountDaoInterface):
        self.account_dao = account_dao

    @abstractmethod
    def service_create_account(self, account:Account2)->Account2:
        pass

    @abstractmethod
    def service_get_account_by_id(self, account_id: str) -> Account2:
        pass

    @abstractmethod
    def service_get_all_accounts_by_customer_id(self, customer_id: str) -> list[Account2]:
        pass

    @abstractmethod
    def service_withdraw(self, account_id: str, amount: float)->Account2:
        pass

    @abstractmethod
    def service_deposit(self, account_id: str, amount: float)->Account2:
        pass

    @abstractmethod
    def service_transfer(self, sender_id: str, receiver_id: str, amount: float)->bool:
        pass

    @abstractmethod
    def service_delete_account_by_id(self, account_id: str) -> bool:
        pass