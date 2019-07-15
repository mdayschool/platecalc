import unittest
from model import calc

class CalcTestCase(unittest.TestCase):
    def test_getplates_empty(self):
        empty_dict = dict();
        self.assertEqual(empty_dict, calc.get_plates(45))

    def test_getplates_less_than_bar(self):
        with self.assertRaises(calc.LessThanBar):
            calc.get_plates(25)

    def test_getplates_not_divisible(self):
        with self.assertRaises(calc.NotDivisible):
            calc.get_plates(46.25)

    def test_getplates_standard_weights_1(self):
        self.assertEqual({45:1}, calc.get_plates(135))

    def test_getplates_standard_weights_2(self):
        self.assertEqual({45:1, 25:1}, calc.get_plates(185))

    def test_getplates_standard_weights_3(self):
        self.assertEqual({45:1, 25:1, 2.5:1}, calc.get_plates(190))


