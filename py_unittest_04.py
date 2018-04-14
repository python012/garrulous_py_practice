#!/usr/bin/env python3

from unittest import TestCase
from unittest.mock import patch
from unittest import main


def func_1():
    func_2()


def func_2():
    print("It's func 2!")


def test_func_1():
    with patch('func_2') as mocked_func_2:
        func_1()
        mocked_func_2.assert_called_once()


if __name__ == '__main__':
    main()