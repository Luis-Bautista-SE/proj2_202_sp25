import unittest
from proj2 import *

class TestRegionFunctions(unittest.TestCase):


    def test_read_csv(self):
        head = read_csv_lines("sample2.csv")
        self.assertIsNotNone(head)

    def test_listlen(self):
        head = read_csv_lines("sample2.csv")
        self.assertEqual(listlen(head), 8)

    def test_filter_year(self):
        head = read_csv_lines("sample2.csv")
        result = filter_rows(head, "year", "greater_than", 2010)
        # Count results
        self.assertEqual(listlen(result), 2)

    def test_filter_country(self):
        head = read_csv_lines("sample2.csv")
        result = filter_rows(head, "country", "equal", "USA")
        self.assertEqual(listlen(result), 3)

if __name__ == '__main__':
    unittest.main()

