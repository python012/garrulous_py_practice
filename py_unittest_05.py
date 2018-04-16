from unittest import TestCase
from unittest.mock import patch
from unittest import main
from person import Person

class FuncTest(TestCase):
    def test_print_parents(self):
        john = Person('John')
             
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Jo', 'Lee')
            with patch('builtins.print') as mocked_print:
                # with patch.object(person.Person, "fake_func") as mocked_fake_func:
                with patch('person.Person.fake_func') as mocked_fake_func:
                    john.print_parents()
                    mocked_print.assert_called_with("John's parents are Jo and Lee.")
                    mocked_fake_func.assert_called_once()


if __name__ == '__main__':
    main()
