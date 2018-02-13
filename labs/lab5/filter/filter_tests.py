import unittest
import filter

class TestCases(unittest.TestCase):

    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    def test_1(self):
        l1 = [1, -1, 2, -2, 3, -3]
        l2 = filter.are_positive(l1)
        self.assertListAlmostEqual(l2, [1, 2, 3])
        l1 = [11, -1, 2, -2, -3, -3]
        l2 = filter.are_positive(l1)
        self.assertListAlmostEqual(l2, [11, 2])

    def test_2(self):
        l1 = [1, 2, 3, 4, 5, 6]
        l2 = filter.are_greater_than_n(3, l1)
        self.assertListAlmostEqual(l2, [4, 5, 6])
        l1 = [1, 2, 3, 4, 5, 6]
        l2 = filter.are_greater_than_n(4, l1)
        self.assertListAlmostEqual(l2, [5, 6])

    def test_3(self):
        l1 = [1, 2, 3, -4, 5, 6]
        l2 = filter.are_divisible_by_n(2, l1)
        self.assertListAlmostEqual(l2, [2, -4, 6])
        l1 = [1, 2, 3, 4, 5, 6]
        l2 = filter.are_divisible_by_n(3, l1)
        self.assertListAlmostEqual(l2, [3, 6])

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

