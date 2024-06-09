from controller import Controller, handle_controller
from controller_util import is_user_allowed

inv_control = Controller("inv", security_checker=is_user_allowed,
                         allowed_gets=[{"name": "acc_id", "arg": "acc_id", "comparator": "="}])


def inv_handle():
    return handle_controller(inv_control)
