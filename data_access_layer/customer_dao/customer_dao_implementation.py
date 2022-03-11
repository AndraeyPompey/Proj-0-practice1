from data_access_layer.customer_dao.customer_dao_interface import CustomerDAOInterface
from entities.customer_class import Customer


class CustomerDAOImp(CustomerDAOInterface):
    def insert_into_customers_table(self, customer_obj: Customer) -> Customer:
        pass

    def delete_from_customers_table_by_id(self, cust_id: int) -> bool:
        pass