import unittest
from math_quiz import function_A, function_B, function_C

class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # Assuming function_B processes an arithmetic operation
        # Replace with actual details of what function_B is supposed to do
        result = function_B(5, 3, '*')  # Example usage with multiplication
        self.assertEqual(result, 15)    # Expected outcome for 5 * 3
        
        result = function_B(8, 4, '-')  # Example usage with subtraction
        self.assertEqual(result, 4)     # Expected outcome for 8 - 4

    def test_function_C(self):
        # Assuming function_C returns a tuple (formatted problem, answer)
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 5, '-', '10 - 5', 5),
            (6, 3, '*', '6 * 3', 18),
            (9, 3, '/', '9 / 3', 3)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = function_C(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
