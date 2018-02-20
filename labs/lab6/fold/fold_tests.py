import unittest
import fold


class TestCases(unittest.TestCase):
    def test_1(self):
        l1 = [1, 2, 3, 4, 5]
        self.assertEqual(fold.sum(l1), 15)
        l2 = [10, 15, 20, 30, 40, 50]
        self.assertEqual(fold.sum(l2), 165)

    def test_2(self):
        l1 = [2, 3, 1, 4, 5]
        self.assertEqual(fold.index_of_smallest(l1), 1)
        l2 = [10, 15, 20, 30, 40, 50]
        self.assertEqual(fold.index_of_smallest(l2), 10)


if __name__ == '__main__':
    unittest.main()

