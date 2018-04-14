#!/usr/bin/env python3

from unittest import TestCase
from unittest.mock import patch
from unittest import main


class Person(object):
    def __init__(self, name):
        self.name = name
    
    def print_name(self):
        print('My name is ' + self.name)

class FuncTest(TestCase):
    def test_print_name01(self):
        john = Person('John')

        with patch('builtins.print') as mocked_print:
            john.print_name()
            mocked_print.assert_called_with('My name is John')

    def test_print_name02(self):
        john = Person('Donald')

        with patch('builtins.print') as mocked_print:
            john.print_name()
            mocked_print.assert_called_with('My name is Donald')

if __name__ == '__main__':
    main()
