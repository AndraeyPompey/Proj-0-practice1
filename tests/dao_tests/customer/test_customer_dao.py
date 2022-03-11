from data_access_layer.customer_dao.customer_dao_implementation import CustomerDAOImp
from entities.customer_class import Customer

customer_dao = CustomerDAOImp()


def test_create_customer_record_success():
    test_customer = Customer(0, "Bobby", "Hill")
    returned_customer = customer_dao.insert_into_customers_table(test_customer)
    assert returned_customer.cust_id != test_customer.cust_id
    #pass a customer object into create method

def test_delete_customer_record_success():
    result = customer_dao.delete_from_customers_table_by_id(-1)
    assert result
    # i need the id of a customer in the database i want to delete
    # pass that id into the delete method
