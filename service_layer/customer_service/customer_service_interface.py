from abc import ABC, abstractmethod

from data_access_layer.customer_dao.customer_dao_interface import CustomerDAOInterface
from entities.customer_class import Customer


class CustomerServiceInterface(ABC):

    def __init__(self, customer_dao: CustomerDAOInterface):
        self.customer_dao = customer_dao

    @abstractmethod
    def service_create_customer_record(self, customer: Customer)->Customer:
        pass

    @abstractmethod
    def service_delete_customer_record(self, cust_id)->bool:
        pass