from unittest import TestCase
from unittest.mock import patch
from unittest import main
     
     
class Person(object):
    def __init__(self, name):
        self.name = name
        
    def print_name(self):
        print('My name is ' + self.name)
        
    def print_parents(self):
        mother = input("Enter mother's name: ")
        father = input("Enter father's name: ")
     
        print("{}'s parents are {} and {}.".format(self.name, mother, father))
        self.fake_func()

    def fake_func(self):
        pass

class FuncTest(TestCase):
    def test_print_parents(self):
        john = Person('John')
             
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Jo', 'Lee')
            with patch('builtins.print') as mocked_print:
                with patch.object(Person, "fake_func") as mocked_fake_func:
                # with patch('Person.fake_func') as mocked_fake_func:
                    john.print_parents()
                    mocked_print.assert_called_with("John's parents are Jo and Lee.")
                    mocked_fake_func.assert_called_once()
 
if __name__ == '__main__':
    main()
