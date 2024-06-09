from controller import Controller, handle_controller


users_to_acc_control = Controller("acc_users")


def users_to_acc_handle():
    return handle_controller(users_to_acc_control)