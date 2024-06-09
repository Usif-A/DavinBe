from flask import Blueprint, request, jsonify
from controller import Controller, handle_controller
from Db import Database as Db
import types
from controller_util import get_with_acc_check,is_token_valid,is_user_allowed


allowed = [
    {"name": "id", "arg": "id", "comparator": "="},
    {"name": "price", "arg": "price-under", "comparator": "<"},
    {"name": "price", "arg": "price-over", "comparator": ">"},
    {"name": "on_discount", "arg": "on-discount", "comparator": "="},
    {"name": "acc_id", "arg": "acc_id", "comparator": "="}
]
item_control = Controller("items", security_checker=is_user_allowed, allowed_gets=allowed)




#item_control.get = types.MethodType(get_with_acc_check, item_control)


def item_handle():
    return handle_controller(item_control)
