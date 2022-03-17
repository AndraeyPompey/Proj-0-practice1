from custom_exceptions.bad_customer_info import BadCustomerInfo
from data_access_layer.customer_dao.customer_dao_interface import CustomerDAOInterface
from entities.customer_class import Customer
from service_layer.customer_service.customer_service_interface import CustomerServiceInterface


class CustomerServiceImp(CustomerServiceInterface):



    def service_create_customer_record(self, customer: Customer):
        if type(customer.first_name) != str or type(customer.last_name) != str:
            raise BadCustomerInfo("customer information is poorly formatted, please try again")
        elif len(customer.first_name) >20 or len(customer.last_name) > 20:
            raise BadCustomerInfo("customer information is poorly formatted, please try again")
        else:
            return self.customer_dao.insert_into_customers_table(customer)

    def service_delete_customer_record(self, cust_id):
        try:
            return self.customer_dao.delete_from_customers_table_by_id(int(cust_id))
        except ValueError:
            raise BadCustomerInfo("customer information is poorly formatted, please try again")
