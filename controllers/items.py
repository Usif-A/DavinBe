from flask import Blueprint, request
from controller import Controller, handle_controller

allowed = [
    {"name": "id", "arg": "id", "comparator": "="},
    {"name": "price", "arg": "price-under", "comparator": "<"},
    {"name": "price", "arg": "price-over", "comparator": ">"},
    {"name": "on_discount", "arg": "on-discount", "comparator": "="}
]

def validate_data():
    pass

item_control = Controller("items", allowed_gets=allowed)


def item_handle():
    return handle_controller(item_control)
