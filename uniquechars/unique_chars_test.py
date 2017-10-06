from unique_chars import unique_characters
import unittest

class AnagramTest(unittest.TestCase):

    def test_a_string(self):
        my_text = unique_characters("anagram")
        self.assertEqual(my_text, ['n', 'g', 'r', 'm'])

    def test_a_string2(self):
        my_text = unique_characters("pacal")
        self.assertEqual(my_text, ['p', 'c', 'l'])
    
    def test_empty_string(self):
        my_text = unique_characters("")
        self.assertEqual(my_text, "no string given")


if __name__ == '__main__':
    unittest.main()