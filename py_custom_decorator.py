#!/usr/bin/env python3

import functools

def my_decorator(func):

    @functools.wraps(func)
    def run():
        print("begin")
        func()
        print("end")
    return run

@my_decorator
def my_run():
    print("just say something")

my_run()
