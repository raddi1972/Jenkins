
import unittest

from leap_year import leap_year_tester

class TestSum(unittest.TestCase):

    def test4(self):
        """
        Test case to add two numbers
        """
        data = 1800
        result = leap_year_tester(data)
        self.assertEqual(result, True)

    def test5(self):
        """
        Test case to add two numbers
        """
        data = 1600
        result = leap_year_tester(data)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
