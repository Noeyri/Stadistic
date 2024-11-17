import unittest
from unittest.mock import patch
from input import input_data

class TestInput(unittest.TestCase):

    @patch('builtins.input', side_effect=['3', '30', '10', '20'])
    def test_return_sorted_data(self, mock_input):
        result = input_data()
        self.assertEqual(result, [10, 20, 30])

    @patch('builtins.input', side_effect=['0'])
    def test_input_data_zero(self, mock_input):
        result = input_data()
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()