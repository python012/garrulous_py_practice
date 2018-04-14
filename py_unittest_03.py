#!/usr/bin/env python3

from unittest import TestCase
from unittest.mock import patch
from unittest import main


def func_input():
    name = input("Enter your name: ")
    print('Your name is {}'.format(name))


def test_func_input():
    with patch('builtins.input') as mocked_input:
        mocked_input.side_effect = ('Jo',)
        with patch('builtins.print') as mocked_print:
            func_input()
            mocked_print.assert_called_with('Your name is Jo')


if __name__ == '__main__':
    main()
