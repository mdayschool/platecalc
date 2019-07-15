import unittest
from model import calc

class GetPlatesTestCase(unittest.TestCase):
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

    def test_getplates_custom_bar(self):
        self.assertEqual({25:1}, calc.get_plates(75, 25))

    def test_getplates_custom_bar_lessthanbar(self):
        with self.assertRaises(calc.LessThanBar):
            calc.get_plates(12, 25)

    def test_getplates_custom_plates(self):
        self.assertEqual({45:1, 1.25:1},
                         calc.get_plates(137.5, 45, [45,25,10,5,2.5,1.25]))

    def test_getplates_custom_plates_unordered(self):
        self.assertEqual({45:1, 1.25:1},
                         calc.get_plates(137.5, 45, [10,25,45,5,2.5,1.25]))

class GetListTestCase(unittest.TestCase):
    def test_getlist_standard(self):
        self.assertEqual([10,5,2.5,1.25], calc.get_list('10, 5, 2.5, 1.25'))
