from controller import Controller, handle_controller


store_to_inv_control = Controller("store_inv")


def store_to_inv_handle():
    return handle_controller(store_to_inv_control)