import unittest
from model import calc

class CalcTestCase(unittest.TestCase):
    def test_getplates_empty(self):
        empty_dict = dict();
        self.assertEqual(empty_dict, calc.get_plates(0))
