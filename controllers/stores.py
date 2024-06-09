from flask import Blueprint, request,jsonify

from controller import Controller, handle_controller

from controller_util import is_user_allowed

store_control = Controller("stores",security_checker=is_user_allowed ,allowed_gets=[{"name": "acc_id", "arg": "acc_id", "comparator": "="}])






def store_handle():
    return handle_controller(store_control)