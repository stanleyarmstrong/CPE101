import unittest
from list_comp import *
from objects import *

class TestCases(unittest.TestCase):

    def test_distance_all(self):
        l_points = [Point(3, 4), Point(6, 8)]
        found = distance_all(l_points)
        expected = [5, 10]
        self.assertEqual(found, expected)
        l_points = [Point(6, 8), Point(9, 12)]
        found = distance_all(l_points)
        expected = [10, 15]
        self.assertEqual(found, expected)

    def test_are_in_first_quadrant(self):
        l_points = [Point(3, 4), Point(6, 8)]
        found = are_in_first_quadrant(l_points)
        expected = [Point(3, 4), Point(6, 8)]
        self.assertEqual(found, expected)
        l_points = [Point(3, 4), Point(-6, 8)]
        found = are_in_first_quadrant(l_points)
        expected = [Point(3, 4)]
        self.assertEqual(found, expected)





# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

