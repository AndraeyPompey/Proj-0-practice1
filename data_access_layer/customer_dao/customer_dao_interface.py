from abc import ABC, abstractmethod

from entities.customer_class import Customer


class CustomerDaoInterface(ABC):

    @abstractmethod
    def insert_into_customers_table(self, customer_obj: Customer) -> Customer:
        pass

    @abstractmethod
    def delete_from_customers_table_by_id(self, cust_id: int) -> bool:
        pass

