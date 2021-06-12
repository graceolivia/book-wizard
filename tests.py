import unittest

from wizard import *

# must figure out how to import these cases

class YesNo(unittest.TestCase):

   def test_yn_y(self):
       result = v_yn("y", "Question:")
       self.assertEqual(result, True)

   def test_yn_n(self):
       result = v_yn("n", "Question:")
       self.assertEqual(result, True)

   def test_too_high_wrong_num(self):
       result = list_val("6", "Question:")
       self.assertEqual(result, False)

   def test_too_high_string(self):
       result = list_val("beans", "Question:")
       self.assertEqual(result, False)

   def test_user_input_5_num(self):
       result = list_val("5", "Question:")
       self.assertEqual(result, True)


       # MUST REDO TO MAKE THINGS ONLY DO ONE THING. MODULARIZE MORE

       # need UNITTEST for 1-5 input


       # unittest 
if __name__ == '__main__':
    unittest.main()