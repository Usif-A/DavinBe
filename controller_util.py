from flask import Blueprint, request, jsonify
from Db import Database as Db
from controller import Controller, handle_controller
import os
import jwt


## Secruity Checks


def is_token_valid():
    try:
        secret_key = os.getenv("TOKEN_KEY")
        jwt.decode(request.headers.get('Authorization').split()[1], secret_key, algorithms=['HS256'])
        return True
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"})
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token"})
    except AttributeError:
        return jsonify({"message": "no token was provided"})


def check_user(account_id, user_id):
    try:
        result = Db.query(
            f"SELECT COUNT(*) > 0 as is_allowed  from acc_users au where au.acc_id ='{account_id}' and au.user_id ='{user_id}'")
        print(result)
        return result[0]["is_allowed"]
    except:
        return False


def is_user_allowed():
    try:
        secret_key = os.getenv("TOKEN_KEY")
        token = jwt.decode(request.headers.get('Authorization').split()[1], secret_key, algorithms=['HS256'])

    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"})
    except jwt.InvalidTokenError:
        return jsonify({"message": "Invalid token"})
    except AttributeError:
        return jsonify({"message": "no token was provided"})

    if request.args.get("acc_id") is None:
        return jsonify({"message": "You are not authorized to call this account / enter an account_id"})
    return check_user(request.args.get("acc_id"), token["user_id"])



## validate_data functions


## get functions

def get_with_acc_check(controller):
    try:
        if not controller.check_token(request.headers.get('Authorization').split()[1]):
            return jsonify({"message": controller.user})  # returns an error message
    except:
        return jsonify({"message": "no token was provided"})
    sql_where = f"where status = 'ACTIVE' "
    if request.args.get("acc_id") is None:
        return jsonify({"message": "You are not authorized to call this account / enter an account_id"})
    controller.isUserAllowed(request.args.get("acc_id"), controller.user["user_id"])

    for col in controller.alq + [{"name": "acc_id", "arg": "acc_id", "comparator": "="}]:
        arg = request.args.get(col["arg"])
        if arg: sql_where += f"and {col["name"]} {col["comparator"]} '{arg}'"

    data = {"data": Db.query(f"select * from {controller.table_name} {sql_where};")}
    return jsonify(data)
