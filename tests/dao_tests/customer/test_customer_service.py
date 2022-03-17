from custom_exceptions.bad_customer_info import BadCustomerInfo
from data_access_layer.customer_dao.customer_dao_implementation import CustomerDAOImp
from entities.customer_class import Customer
from service_layer.customer_service.customer_service_imp import CustomerServiceImp

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)



def test_catch_non_string_first_name():
    try:
        customer = Customer(0, 40, "thiscool")
        customer_service.service_create_customer_record(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Please enter a valid name"



def test_catch_non_string_last_name():
    try:
        customer = Customer(0, "thiscool", 40)
        customer_service.service_create_customer_record(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Please enter a valid name"

def test_catch_first_name_too_long():
    try:
        customer = Customer(0, "nooooooooooooooooooooooooooooooooooooooooooooooel", "thiscool")
        customer_service.service_create_customer_record(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Please enter a valid name"

def test_catch_last_name_too_long():
    try:
        customer = Customer(0, "willie", "thiscooooooooooooooooooooooooooooooooooooooooooooool")
        customer_service.service_create_customer_record(customer)
        assert False
    except BadCustomerInfo as e:
        assert str(e) == "Please enter a valid name"