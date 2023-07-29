import unittest
import functions


class TestFunctions(unittest.TestCase):

    def test_format_numbers(self):
        self.assertEqual(functions.format_numbers(""), None)
        self.assertEqual(functions.format_numbers("Maestro 1596837868705199"), ("1596 83** **** 5199", "Maestro"))
        self.assertEqual(functions.format_numbers("Счет 64686473678894779589"), ("**9589", "Счет"))
