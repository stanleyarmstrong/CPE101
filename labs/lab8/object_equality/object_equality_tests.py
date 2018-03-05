import unittest
from objects import *

class TestCases(unittest.TestCase):
    def test_equality(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        c1 = Circle(p1, 2)
        c2 = Circle(p1, 2)
        self.assertEqual(p1, p2)
        self.assertEqual(c1, c2)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

