import unittest
import string_101


class TestString(unittest.TestCase):
    def test_rot_13(self):
        string1 = 'hello'
        self.assertEqual(string_101.str_rot_13(string1), 'uryyb')
        string2 = 'uryyb'
        self.assertEqual(string_101.str_rot_13(string2), 'hello')

    def test_translate_101(self):
        string1 = 'abcdcba'
        self.assertEqual(string_101.str_translate_101(string1, 'a', 'x'), 'xbcdcbx')
        string2 = 'hello'
        self.assertEqual(string_101.str_translate_101(string2, 'l', 'ff'), 'heffffo')

if __name__ == '__main__':
    unittest.main()

