import unittest;
import sys
import os
sys.path.insert(0, os.path.abspath('./calc_module'))
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 15), 25)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-10, -45), -55)
    
    def test_divide(self):
        self.assertEqual(calc.divide(20, 2), 10)
        self.assertEqual(calc.divide(5, 2), 2.5)
        
        self.assertRaises(ValueError, calc.divide, 12, 0)


if __name__ == '__main__':
    unittest.main()