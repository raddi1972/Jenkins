
import unittest

from leap_year import leap_year_tester

class TestSum(unittest.TestCase):
    def test1(self):
        """
        Test case to add two numbers
        """
        data = 2000
        result = leap_year_tester(data)
        self.assertEqual(result, True)

    def test2(self):
        """
        Test case to add two numbers
        """
        data = 2020
        result = leap_year_tester(data)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
