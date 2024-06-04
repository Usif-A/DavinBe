from flask import Blueprint, request
from controller import Controller, handle_controller


acc_control = Controller("accounts")


def acc_handle():
    return handle_controller(acc_control)