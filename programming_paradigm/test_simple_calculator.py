import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(100, 200), 300)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(100, 50), 50)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(100, 1), 100)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2.0)
        self.assertEqual(self.calc.divide(-6, 3), -2.0)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(100, 5), 20.0)
        
        # Test division by zero
        self.assertEqual(self.calc.divide(10, 0), None)
        self.assertEqual(self.calc.divide(0, 0), None)

    def test_edge_cases(self):
        """Test edge cases for division."""
        # Large numbers for division
        self.assertEqual(self.calc.divide(1000000, 5000), 200.0)
        self.assertEqual(self.calc.divide(10**10, 1), 10**10)
        
        # Very small decimal numbers
        self.assertEqual(self.calc.divide(0.0001, 0.0002), 0.5)
        self.assertEqual(self.calc.divide(0.0001, 0.00001), 10.0)

if __name__ == "__main__":
    unittest.main()

