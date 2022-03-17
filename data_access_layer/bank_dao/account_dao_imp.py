from data_access_layer.bank_dao.account_dao_interface import AccountDaoInterface
from entities.account_class import Account


class AccountDaoImp(AccountDaoInterface):
    def create_account_record(self, account: Account) -> Account:
        pass

    def select_account_by_id(self, account_id: int) -> Account:
        pass

    def select_all_accounts_by_customer_id(self, cust_id: int) -> list[Account]:
        pass

    def update_account_by_id(self, account: Account) -> Account:
        pass

    def transfer_funds(self, sender_id: int, receiver_id: int, amount: float):
        pass

    def delete_account_by_id(self, account_id: int) -> bool:
        pass