#!/usr/bin/env python3

import functools

def check_is_verified_user(user_name):
    def my_decorator_with_arg(func):
        @functools.wraps(func)
        def check_and_run():
            print("begin")
            if user_name == "logined_user":
                func()
            else:
                print("Sorry! You're not logined user!")
            print("end")
        return check_and_run
    return my_decorator_with_arg


@check_is_verified_user("not_logined_user")
def show_user_page():
    print("Welcome! User page is launched!")

show_user_page()
