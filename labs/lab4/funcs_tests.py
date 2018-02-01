import funcs
import unittest

class TestCases(unittest.TestCase):
    def test_max_101(self):
        found = funcs.max_101(2 ,1)
        expected = 2
        self.assertEqual(found , expected)

        found = funcs.max_101(2 , 3)
        expected = 3
        self.assertEqual(found, expected)

        found = funcs.max_101(3 , 4)
        expected = 4
        self.assertEqual(found, expected)

    def test_max_of_three(self):
        found = funcs.max_of_three(1 ,2 ,3)
        expected = 3
        self.assertEqual(found, expected)

        found = funcs.max_of_three(4 , 6 , 5)
        expected = 6
        self.assertEqual(found , expected)

        found = funcs.max_of_three(10, 9, 8)
        expected = 10
        self.assertEqual(found, expected)

        found = funcs.max_of_three(11 , 11 ,11)
        expected = 11
        self.assertEqual(found, expected)

    def test_repeat_max_of_three(self):
        funcs.repeated_max_of_three()



if __name__ == '__main__':
    unittest.main()
