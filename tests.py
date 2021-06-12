import unittest

from wizard import *


class YesNo(unittest.TestCase):

   def test_yn_y(self):
       result = v_yn("y")
       self.assertEqual(result, True)

   def test_yn_n(self):
       result = v_yn("n")
       self.assertEqual(result, True)

   def test_too_high_wrong_num(self):
       result = list_val("6")
       self.assertEqual(result, False)

   def test_too_high_string(self):
       result = list_val("beans")
       self.assertEqual(result, False)

   def test_user_input_5_num(self):
       result = list_val("5")
       self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()