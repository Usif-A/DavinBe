from flask import Flask, make_response, request
from controllers.items import item_handle
from controllers.users import user_handle,login_handle
from controllers.accounts import acc_handle


app = Flask(__name__)


app.add_url_rule('/users', view_func=user_handle, methods=['GET', 'POST', 'PUT', 'DELETE'])
app.add_url_rule('/items', view_func=item_handle, methods=['GET', 'POST', 'PUT', 'DELETE'])
app.add_url_rule('/users/login', view_func=login_handle , methods=['POST'])
app.add_url_rule('/accounts', view_func=acc_handle, methods=['GET', 'POST', 'PUT', 'DELETE'])


@app.route("/")
def hello_world():
    return "hello world"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
