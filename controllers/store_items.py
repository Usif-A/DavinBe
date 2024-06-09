from controller import Controller, handle_controller


store_to_item_control = Controller("store_items")


def store_to_item_handle():
    return handle_controller(store_to_item_control)