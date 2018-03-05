import unittest
from objects import *
import funcs_objects


class TestObjects(unittest.TestCase):
    def test_point(self):
        p1 = Point(1, 2)
        self.assertEqual(p1.x, 1)
        self.assertEqual(p1.y, 2)

    def test_distance(self):
        p1 = Point(1, 2)
        p2 = Point(4, 6)
        found = funcs_objects.distance(p1, p2)
        expected = 5
        self.assertEqual(found, expected)

    def test_circle(self):
        center1 = Point(3, 2)
        center2 = Point(4, 6)
        c1 = Circle(center1, 4)
        c2 = Circle(center2, 5)
        self.assertEqual(c1.center, center1)
        self.assertEqual(c2.center, center2)
        self.assertEqual(c1.radius, 4)
        self.assertEqual(c2.radius, 5)

    def test_overlap(self):
        center1 = Point(3, 2)
        center2 = Point(4, 6)
        center3 = Point(7, 10)
        center4 = Point(8, 15)
        c1 = Circle(center1, 5)
        c2 = Circle(center2, 2)
        c3 = Circle(center3, 4)
        c4 = Circle(center4, 3)
        overlap1 = funcs_objects.circles_overlap(c1, c2)
        overlap2 = funcs_objects.circles_overlap(c1, c3)
        overlap3 = funcs_objects.circles_overlap(c1, c4)
        self.assertTrue(overlap1)
        self.assertTrue(overlap2)
        self.assertFalse(overlap3)


if __name__ == '__main__':
    unittest.main()