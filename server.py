from flask import Flask, make_response, request
from flask_cors import CORS
from controllers.items import item_handle
from controllers.users import user_handle,login_handle
from controllers.accounts import acc_handle
from controllers.stores import store_handle
from controllers.store_items import store_to_item_handle
from controllers.orders import order_handle
from controllers.mods import order_modification_handle
from controllers.inv import inv_handle
from controllers.store_inv import store_to_inv_handle
from controllers.acc_users import users_to_acc_handle

app = Flask(__name__)
CORS(app)

app.add_url_rule('/users',       view_func=user_handle, methods=['GET', 'POST', 'PUT', 'DELETE'])
app.add_url_rule('/users/login', view_func=login_handle, methods=['POST'])
app.add_url_rule('/accounts',    view_func=acc_handle, methods=['GET', 'POST', 'PUT', 'DELETE'])
app.add_url_rule('/accusers',    view_func=users_to_acc_handle, methods=['GET', 'POST', 'PUT', 'DELETE'])

app.add_url_rule('/items',       view_func=item_handle, methods=['GET', 'POST', 'PUT', 'DELETE'])
app.add_url_rule('/stores',      view_func=store_handle, methods=['GET', 'POST', 'PUT', 'DELETE'])
app.add_url_rule('/storeitems',  view_func=store_to_item_handle, methods=['GET', 'POST', 'PUT', 'DELETE'])

app.add_url_rule('/inv',      view_func=inv_handle, methods=['GET', 'POST', 'PUT', 'DELETE'])
app.add_url_rule('/storeinv',      view_func=store_to_inv_handle, methods=['GET', 'POST', 'PUT', 'DELETE'])

app.add_url_rule('/orders',      view_func=order_handle, methods=['GET', 'POST', 'PUT', 'DELETE'])
app.add_url_rule('/mods',      view_func=order_modification_handle, methods=['GET', 'POST', 'PUT', 'DELETE'])



@app.route("/")
def hello_world():
    return "hello world"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
