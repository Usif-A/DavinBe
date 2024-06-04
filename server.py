from flask import Flask, make_response, request
from controllers.items import item_handle


app = Flask(__name__)




app.add_url_rule('/items', view_func=item_handle, methods=['GET', 'POST', 'PUT', 'DELETE'])

@app.route("/")
def hello_world():
    return "hello world"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
