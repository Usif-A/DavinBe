
from controller import Controller, handle_controller
from controller_util import is_user_allowed

order_control = Controller("orders", security_checker=is_user_allowed, allowed_gets=[{"name": "acc_id", "arg": "acc_id", "comparator": "="}])


def order_handle():
    return handle_controller(order_control, )