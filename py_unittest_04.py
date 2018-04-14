#!/usr/bin/env python3

from unittest import TestCase
from unittest.mock import patch
from unittest import main


def func_1():
    return 'Hello ' + func_2()


def func_2():
    return 'Hello'


def test_func_1():
    with patch('func_2', return_value='World!'):
        assert func_1() == 'Hello World!'



if __name__ == '__main__':
    main()