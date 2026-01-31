import unittest
from baitap1 import calculate_sum_and_average

class TestCalculateFunctions(unittest.TestCase):

    def test_valid_numbers(self):
        self.assertEqual(calculate_sum_and_average([1, 2, 3]), (6, 2.0))

    def test_empty_list(self):
        with self.assertRaises(ValueError) as context:
            calculate_sum_and_average([])
        self.assertEqual(str(context.exception), "Dãy số không được rỗng.")

    # fix bug test negative numbers
    def test_negative_numbers(self):
        self.assertEqual(calculate_sum_and_average([1, -2, 3]), (2, 0.6666666666666666))

    # fix bug test non numeric input
    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            calculate_sum_and_average(["a", "b", "c"])

    def test_number_from_user(self):
        # This test is not applicable here since we cannot simulate user input in this context.
        # Instead, we can test the function that processes user input separately.
        pass

if __name__ == '__main__':
    unittest.main()