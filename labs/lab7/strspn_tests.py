import unittest
import strspn

class TestCases(unittest.TestCase):

    def test_my_strspn(self):
        found = strspn.my_strspn('calpoly', 'california')
        expected = 3
        self.assertEqual(found, expected)
        found = strspn.my_strspn('calpoly', 'place')
        expected = 4
        self.assertEqual(found, expected)
        found = strspn.my_strspn('cccca', 'office')
        expected = 4
        self.assertEqual(found, expected)
        found = strspn.my_strspn('minute', 'simulation')
        expected = 5
        self.assertEqual(found, expected)
        found = strspn.my_strspn(1234, 1234)
        expected = 0
        self.assertEqual(found, expected)
        found = strspn.my_strspn('calpoly', 'calPOLY')
        expected = 3
        self.assertEqual(found, expected)


if __name__ == '__main__':
    unittest.main()