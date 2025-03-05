# Run command: python -m unittest Evaluate_Reverse_Polish_Nation_Test.py 

import unittest
from Evaluate_Reverse_Polish_Nation import Solution

class TestEvaluateReversePolishNotation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        result = self.solution.evalRPN(tokens)
        self.assertEqual(result, 22)

    def test_single_number(self):
        tokens = ["3"]
        result = self.solution.evalRPN(tokens)
        self.assertEqual(result, 3)

    def test_addition(self):
        tokens = ["2", "1", "+"]
        result = self.solution.evalRPN(tokens)
        self.assertEqual(result, 3)

    def test_subtraction(self):
        tokens = ["4", "2", "-"]
        result = self.solution.evalRPN(tokens)
        self.assertEqual(result, 2)

    def test_multiplication(self):
        tokens = ["2", "3", "*"]
        result = self.solution.evalRPN(tokens)
        self.assertEqual(result, 6)

    def test_division(self):
        tokens = ["8", "4", "/"]
        result = self.solution.evalRPN(tokens)
        self.assertEqual(result, 2)

    def test_complex_expression(self):
        tokens = ["4", "13", "5", "/", "+"]
        result = self.solution.evalRPN(tokens)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()