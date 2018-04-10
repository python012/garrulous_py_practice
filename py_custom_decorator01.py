#!/usr/bin/env python3

import functools

def check_is_verified_user(user_name):
    def my_decorator_with_arg(func):
        @functools.wraps(func)
        def check_and_run(*args, **kwargs):
            print("begin")
            if user_name == "logined_user":
                func(*args, **kwargs)
            else:
                print("Sorry! You're not logined user!")
            print("end")
        return check_and_run
    return my_decorator_with_arg


@check_is_verified_user("logined_user")
def show_user_page(x, y):
    print("Welcome! User page is launched!")
    print(x + y)

show_user_page(70, 98)
