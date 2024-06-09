import bcrypt
from controller import Controller, handle_controller
from flask import request
from Db import Database as Db
from flask import Flask, request, jsonify

from datetime import datetime, timedelta, timezone
import os
from dotenv import load_dotenv
import jwt


load_dotenv()


def validate_data(body):
    password = body["password"].encode("utf-8")
    # Adding the salt to password
    salt = bcrypt.gensalt()
    # Hashing the password
    hashed = bcrypt.hashpw(password, salt)
    body["passhash"] = hashed
    body.pop("password", None)
    return body


user_control = Controller("users", modify_data=validate_data ,allowed_gets=[{"name": "email", "arg": "email", "comparator": "="}])
def user_handle():
    return handle_controller(user_control)


# Checking if the provided password matches the stored hash
# input_password = b'GeekPassword'  # Example input to check
# is_correct = verify_password(input_password, hashed)
#
# print("Password match:" if is_correct else "Password does not match")
def login_handle():
    return login()

def login():
    sign_data = request.json
    user_data = Db.query(f"select * from users where email = '{sign_data["email"]}'")[0]


    if bcrypt.checkpw(sign_data["password"].encode("utf-8"), user_data["passhash"].encode("utf-8")):
        payload = {
            'user_id': user_data["id"],
            'username': user_data["email"],
            'acc_id': "e4671bd6-ed9b-4d1c-b690-7712f589f702",
            'exp': datetime.utcnow() + timedelta(minutes=60)  # Token expiration time
        }

        # Define the secret key
        secret_key = os.getenv("TOKEN_KEY")

        # Encode the JWT
        token = jwt.encode(payload, secret_key, algorithm='HS256')
        print(f"Encoded JWT: {token}")

        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401




