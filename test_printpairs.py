"""
@author: Mirav Gokani
Unit tests for print_pairs.py
"""
import print_pairs as ps
import unittest


class TestPairs(unittest.TestCase):
    def test_negativenumbers(self):
        result = ps.pairs([-4, 4, 0, -2, 0], 0)
        self.assertEqual(result[0, 0], -4)
        self.assertEqual(result[0, 1], 4)
        self.assertEqual(result[1, 0], 0)
        self.assertEqual(result[1, 1], 0)

    def test_exception(self):
        with self.assertRaises(Exception):
            ps.pairs([1, 1, 1, 2], 5)


if __name__ == "__main__":
    unittest.main()
