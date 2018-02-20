import unittest
import char


class TestChar(unittest.TestCase):
    def test_lower(self):
        char1 = 'a'
        char2 = 'A'
        char3 = 'C'
        char4 = 'b'
        self.assertTrue(char.is_lower_101(char1))
        self.assertFalse(char.is_lower_101(char2))
        self.assertFalse(char.is_lower_101(char3))
        self.assertTrue(char.is_lower_101(char4))

    def test_char_rot_13(self):
        char1 = 'a'
        char2 = 'A'
        char3 = 'n'
        char4 = 'N'
        self.assertEqual(char.char_rot_13(char1), 'n')
        self.assertEqual(char.char_rot_13(char2), 'N')
        self.assertEqual(char.char_rot_13(char3), 'a')
        self.assertEqual(char.char_rot_13(char4), 'A')


if __name__ == '__main__':
    unittest.main()

