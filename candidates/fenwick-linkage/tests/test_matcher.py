"""Unit tests for Fenwick Linkage."""

import unittest

from fenwick_linkage.matcher import resolve


class MatcherTest(unittest.TestCase):
    def test_identical_records(self):
        left = {"email": "a@example.com", "phone": "555-0100", "surname": "Smith", "postcode": "AB1 2CD", "name": "Alice Smith", "address": "1 Main St"}
        right = dict(left)
        self.assertTrue(resolve(left, right))

    def test_clearly_different_records(self):
        left = {"email": "a@example.com", "phone": "555-0100", "surname": "Smith", "postcode": "AB1 2CD", "name": "Alice Smith", "address": "1 Main St"}
        right = {"email": "b@example.org", "phone": "888-9999", "surname": "Jones", "postcode": "ZZ9 9ZZ", "name": "Bob Jones", "address": "9 Other Rd"}
        self.assertFalse(resolve(left, right))


if __name__ == "__main__":
    unittest.main()
