


class Customer:

    def __init__(self, cust_id, first_name, last_name):
        self.cust_id = cust_id
        self.first_name = first_name
        self.last_name = last_name

    def convert_to_dictionary(self):
        return {
            "customerId": self.cust_id,
            "firstName": self.first_name,
            "lastName": self.last_name
        }


