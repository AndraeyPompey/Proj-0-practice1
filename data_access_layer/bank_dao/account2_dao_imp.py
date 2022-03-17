from custom_exceptions.bad_customer_info import BadCustomerInfo
from data_access_layer.bank_dao.account2_dao_interface import Account2DaoInterface
from entities.account_class2 import Account2
from utils.create_connection import connection


class Account2DaoImp(Account2DaoInterface):
    def create_account(self, account2: Account2) -> Account2:
        sql ="insert into accounts values(default, %s, %s) returning account_id"
        cursor = connection.cursor()
        cursor.execute(sql, (account2.customer_id, account2.balance2))
        connection.commit()
        returned_id = cursor.fetchone()[0]
        account2.account2_id = returned_id
        return account2


    def get_account_by_account_id(self, account2_id: int) -> Account2:
        sql = "select * from accounts where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account2_id])
        record = cursor.fetchone()
        if len(record) != 0:
            account = Account2(*record)
            return account
        else:
            raise BadCustomerInfo("No account matches the Id given. try again")

    def get_all_accounts_by_customer_id(self, customer_id: int) -> list[Account2]:
        sql = "select * from accounts where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        records = cursor.fetchall()
        if len(records) is not None:
            accounts = []
            for record in records:
                account = Account2(*record)
                accounts.append(account)
                return accounts
            else:
                raise BadCustomerInfo("No account matches the Id given. try again")

    def update_account_by_account_id(self, account: Account2) -> Account2:
        sql = "update accounts set balance %s where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (account.balance2, account.account2_id))
        connection.commit()
        if cursor.rowcount != 0:
            return account
        else:
            raise BadCustomerInfo("No account matches the Id given. try again")

    def transfer(self, sender_id: int, receiver_id: int, amount: float) -> bool:
        sql1 = "update accounts set balance = balance - %s where account_id = %s"
        sql2 = "update accounts set balance = balance + %s where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql1,(amount,sender_id,amount,receiver_id))
        if cursor.rowcount != 1:
            connection.rollback()
            raise BadCustomerInfo("No account matches the Id given. try again")
        cursor.execute(sql1, (amount, sender_id, amount, sender_id))
        if cursor.rowcount != 1:
            connection.rollback()
            raise BadCustomerInfo("No account matches the Id given. try again")
        return True


        # elif cursor.fetchone()[0] == sender_id:
        #     connection.rollback()
        #     raise BadCustomerInfo("No receiver account matches the Id given. try again")
        # elif:
        #     connection.rollback()
        #     raise BadCustomerInfo("No sender account matches the Id given. try again")




    def delete_account_by_id(self, account2_id: int) -> bool:
        sql = "delete from accounts where account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account2_id])
        if cursor.rowcount != 0:
            return True
        else:
            raise BadCustomerInfo("No account matches the Id given. try again")