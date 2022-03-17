from data_access_layer.customer_dao.customer_dao_interface import CustomerDAOInterface
from entities.customer_class import Customer
from utils.create_connection import connection


class CustomerDAOImp(CustomerDAOInterface):
    def insert_into_customers_table(self, customer_obj: Customer) -> Customer:
        sql = "insert into customers values(default, %s, %s) returning customerId"
        cursor = connection.cursor()
        cursor.execute(sql, (customer_obj.first_name, customer_obj.last_name))
        connection.commit()
        returned_id = cursor.fetchone()[0]
        customer_obj.cust_id = returned_id
        return customer_obj
        # set up sql
        # create cursor
        # use cursor to execute sql transaction
        # remember to commit transaction
        # get the returned generated id
        # assign it to my customer obj
        #return customer obj

    def delete_from_customers_table_by_id(self, cust_id: int) -> bool:
        sql = "delete from customers where customerId = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [cust_id])
        connection.commit()
        if cursor.rowcount != 0:
            return True
        else:
            return False
        #create sql query
        #create cursor object
        #use cursor to execute sql
        #check that the table was affected
        # assuming it was, return true
        # else do something else