from custom_exceptions.nothing_deleted import NothingDeleted
from data_access_layer.customer_dao.customer_dao_implementation import CustomerDAOImp
from entities.customer_class import Customer
from utils.create_connection import connection

customer_dao = CustomerDAOImp()


def test_create_customer_record_success():
    test_customer = Customer(0, "Bobby", "Hill")
    returned_customer = customer_dao.insert_into_customers_table(test_customer)
    assert returned_customer.cust_id != 0
    #pass a customer object into create method

def test_create_customer_with_bad_id():
    customer = Customer(-98987, "Name", "Fine")
    result = customer_dao.insert_into_customers_table(customer)
    assert result.cust_id != 0

def test_delete_customer_record_success():
    result = customer_dao.delete_from_customers_table_by_id(-1)
    assert result
    # i need the id of a customer in the database i want to delete
    # pass that id into the delete method

def test_delete_customer_with_bad_id():
    try:
        customer_dao.delete_from_customers_table_by_id(-1000)
        assert False
    except NothingDeleted as e:
        assert str(e) == "customer information is poorly formatted, please try again"



    # sql = "delete from customers where customerId = %s"
    # cursor = connection.cursor()

