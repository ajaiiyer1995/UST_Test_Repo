import unittest
from src.function1 import func1
from src.function2 import func2

class TestFunctions(unittest.TestCase):
    def test_func1(self):
        self.assertEqual(func1(), "Input for Function 1")

    def test_func2(self):
        self.assertEqual(func2(), "Input for Function 2")

if __name__ == "__main__":
    unittest.main()