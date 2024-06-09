from controller import Controller, handle_controller


order_modification_control = Controller("mods")


def order_modification_handle():
    return handle_controller(order_modification_control)