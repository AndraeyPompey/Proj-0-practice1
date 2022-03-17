from flask import Flask, request, jsonify

from custom_exceptions.bad_customer_info import BadCustomerInfo
from data_access_layer.customer_dao.customer_dao_implementation import CustomerDAOImp
from entities.customer_class import Customer
from service_layer.customer_service.customer_service_imp import CustomerServiceImp

app: Flask = Flask(__name__)

customer_dao = CustomerDAOImp()
customer_service = CustomerServiceImp(customer_dao)

@app.route("/customer", methods=["POST"])
def create_customer_record():
    try:
        customer_info = request.get_json()
        customer = Customer(
            customer_info["customerId"],
            customer_info["firstName"],
            customer_info["lastName"]
        )
        returned_customer = customer_service.service_create_customer_record(customer)
        dictionary_customer = returned_customer.convert_to_dictionary()
        customer_json = jsonify(dictionary_customer)
        return customer_json, 201
    except BadCustomerInfo as e:
        return_message = {
            "message": str(e)
        }
        return jsonify(return_message), 404



@app.route("/customer/<cust_id>", methods=["DELETE"])
def delete_customer_record(cust_id):
    try:
        result = customer_service.service_delete_customer_record(int(cust_id))
        message = {"result":result}
        return jsonify(message), 200
    except BadCustomerInfo as e:
        return_message = {
            "message": str(e)
        }
        return jsonify(return_message), 404


app.run()