import unittest
import map


class TestCases(unittest.TestCase):

    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    def test_1(self):
        l1 = [1, 2, 3, 4]
        l2 = map.square_all(l1)
        self.assertListAlmostEqual(l2, [1, 4, 9, 16])
        l1 = [5, 6, 7, 8]
        l2 = map.square_all(l1)
        self.assertListAlmostEqual(l2 , [25, 36, 49, 64])


    def test_2(self):
        l1 = [1, 3, 6, 9]
        l2 = map.add_n_all(5, l1)
        self.assertListAlmostEqual(l2, [6, 8, 11, 14])
        l1 = [4, 8, 12, 16]
        l2 = map.add_n_all(11, l1)
        self.assertListAlmostEqual(l2, [15, 19, 23, 27])

    def test_3(self):
        l1 = [1, 2, 3, 4, 5, 6]
        l2 = map.even_or_odd_all(l1)
        self.assertListAlmostEqual(l2, [False, True, False, True, False, True])
        l1 = [9, 11, 13, 15, 17, 19, 20]
        l2 = map.even_or_odd_all(l1)
        self.assertListAlmostEqual(l2 , [False, False, False, False, False, False, True])


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

