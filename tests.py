import unittest
import unittest.mock as mock
from io import StringIO
import sys

from wizard import *

# this printout-checking test produced with help from the good people at:
# https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print


def printout_tester_one_arg(function, arg):
    captured = StringIO()         
    sys.stdout = captured             
    function(arg)  
    printed = captured.getvalue().rstrip("\n")           
    sys.stdout = sys.__stdout__  
    return printed 

def printout_tester_no_arg(function):
    captured = StringIO()         
    sys.stdout = captured             
    function()  
    printed = captured.getvalue().rstrip("\n")           
    sys.stdout = sys.__stdout__  
    return printed 


class YesNo(unittest.TestCase):
    def test_yes_or_no_y(self):
        result = validate_yes_or_no("y")
        self.assertEqual(result, True)

    def test_yes_or_no_n(self):
        result = validate_yes_or_no("n")
        self.assertEqual(result, True)

class list_select(unittest.TestCase):

    def test_too_high_wrong_num(self):
        result = validate_1_5("6")
        self.assertEqual(result, False)

    def test_too_high_string(self):
        result = validate_1_5("beans")
        self.assertEqual(result, False)

    def test_user_input_5_num(self):
        result = validate_1_5("5")
        self.assertEqual(result, True)

class user_input_api_validator(unittest.TestCase): 
    def test_user_input_fail(self):
        result = api_call("")
        self.assertEqual(result, False)

class main_menu_tests(unittest.TestCase):

    def test_menu_selector(self):
        with mock.patch('builtins.input', return_value="1"):
            assert menu_choose() == "1"

    def test_menu_print(self):
        menu_string="""----------------------------
| Menu:                    |
| 1. Search For Books      |
| 2. View your reading list|
| 3. Quit                  |
----------------------------"""
        output=printout_tester_no_arg(menu_print)
        self.assertEqual(menu_string, output)

class booklist_print_tests(unittest.TestCase):
    def test_list_print(self):
        test_list = []
        output = printout_tester_one_arg(display_list, test_list)
        self.assertEqual(output, 'No items currently in list.')

if __name__ == '__main__':
    unittest.main()