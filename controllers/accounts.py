from flask import Blueprint, request, jsonify
from Db import Database as Db
from controller import Controller, handle_controller
import types

acc_control = Controller("accounts")

def safe_get(control):
    try:
        if not control.check_token(request.headers.get('Authorization').split()[1]):
            return jsonify({"message": control.user})
    except:
        return jsonify({"message": "no token was provided"})
    uid = control.user["user_id"]
    sql_where = f"and a.status = 'ACTIVE' "
    for col in control.alq:
        arg = request.args.get(col["arg"])
        if arg: sql_where += f"and {col["name"]} {col["comparator"]} '{arg}'"
    data = {"data": Db.query(f"select a.* from acc_users au join accounts a on au.acc_id =a.id where au.user_id = '{uid}' {sql_where}")}
    return jsonify(data)

acc_control.get = types.MethodType(safe_get, acc_control)

def acc_handle():
    return handle_controller(acc_control)